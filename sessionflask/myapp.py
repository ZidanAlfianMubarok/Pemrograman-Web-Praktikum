from flask import Flask, render_template, session, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import bcrypt
from random import randint
app = Flask(__name__)

app.secret_key = '!@#$'  # Ganti dengan kunci yang lebih aman

# Konfigurasi MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sidakaton'
app.config['MYSQL_DB'] = 'flaskmysql'

mysql = MySQL(app)

# Route default dan method HTTP yang diizinkan
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'inpEmail' in request.form and 'inpPass' in request.form:
        email = request.form['inpEmail']
        passwd = request.form['inpPass']
        captcha_answer = request.form['captcha']

        # Cek apakah CAPTCHA dijawab dengan benar
        if 'captcha_answer' not in session or int(captcha_answer) != session['captcha_answer']:
            return render_template('login.html', error='Jawaban CAPTCHA salah')

        # Proses login seperti biasa
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        result = cur.fetchone()

        if result:
            stored_password = result[2]
            if bcrypt.checkpw(passwd.encode('utf-8'), stored_password.encode('utf-8')):
                session['is_logged_in'] = True
                session['username'] = result[1]
                return redirect(url_for('home'))

        return render_template('login.html', error='Invalid email or password')

    # Buat CAPTCHA baru setiap kali halaman di-load
    num1, num2 = randint(1, 10), randint(1, 10)
    session['captcha_question'] = f"{num1} + {num2}"
    session['captcha_answer'] = num1 + num2

    return render_template('login.html')

# Route untuk registrasi
@app.route('/register', methods=['GET', 'POST'])
def register():
    success_message = False
    if request.method == 'POST' and 'inpEmail' in request.form and 'inpPass' in request.form and 'username' in request.form:
        email = request.form['inpEmail']
        passwd = request.form['inpPass']
        username = request.form['username']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cur.fetchone()

        if existing_user:
            return render_template('register.html', error='Email is already registered')
        else:
            hashed_password = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
            cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, hashed_password))
            mysql.connection.commit()
            cur.close()
            success_message = True  # Set success message to True

    return render_template('register.html', success=success_message)

# Route to show the edit form
@app.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
    if 'is_logged_in' in session:
        username = session['username']
        cur = mysql.connection.cursor()

        # Fetch the logged-in user's data
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user_data = cur.fetchone()
        cur.close()

        if request.method == 'POST':
            # Get data from form
            new_username = request.form['username']
            new_email = request.form['email']
            new_password = request.form['password']
            new_address = request.form['address']
            new_phone = request.form['phone']

            # Update the user data in the database
            cur = mysql.connection.cursor()
            cur.execute("""
                UPDATE users SET username=%s, email=%s, password=%s, alamat=%s, nomor_telepon=%s WHERE username=%s
            """, (new_username, new_email, new_password, new_address, new_phone, username))
            mysql.connection.commit()
            cur.close()

            # Update session with the new username
            session['username'] = new_username

            flash('Profile updated successfully!', 'success')
            return redirect(url_for('home'))

        return render_template('edit_profile.html', user=user_data)
    else:
        return redirect(url_for('login'))

# Route home
@app.route('/home')
def home():
    if 'is_logged_in' in session:#sessionnyaa
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users")
        data = cur.fetchall()
        cur.close()
        return render_template('home.html', users=data)
    else:
        return redirect(url_for('login'))

# Route logout
@app.route('/logout')
def logout():
    session.pop('is_logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))

# Debug dan auto reload
if __name__ == '__main__':
    app.run(debug=True)



# Penggunaan bcrypt: Saya telah menambahkan penggunaan bcrypt untuk hashing password. Ini jauh lebih aman daripada menyimpan password dalam bentuk plain text.
# Secret key: Pastikan untuk mengganti app.secret_key dengan nilai yang lebih aman dan acak.
# Validasi input: Tambahkan validasi input untuk memastikan bahwa data yang dimasukkan pengguna sesuai dengan yang diharapkan.
# Prepared statements: Gunakan prepared statements untuk semua query database untuk mencegah SQL injection.
# HTTPS: Pastikan aplikasi berjalan di atas HTTPS di lingkungan produksi.
# Rate limiting: Pertimbangkan untuk menambahkan rate limiting pada rute login untuk mencegah brute force attacks.
# Logout yang aman: Pastikan untuk menghapus semua data sesi saat logout.
# Error handling: Tambahkan error handling yang lebih baik untuk menangani berbagai jenis kesalahan yang mungkin terjadi.
# Konfigurasi database: Simpan konfigurasi database di file terpisah dan jangan masukkan ke dalam version control.
# Debug mode: Pastikan untuk menonaktifkan debug mode di lingkungan produksi.