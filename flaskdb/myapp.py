# Import library third party
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

# Init main app
app = Flask(__name__)

# Database config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sidakaton'
app.config['MYSQL_DB'] = 'flaskmysql'

# Init MySQL
mysql = MySQL(app)

# Set route default
@app.route('/')
# Function home
def home():
    # Cursor koneksi mysql
    cur = mysql.connection.cursor()

    # Eksekusi kueri
    cur.execute("SELECT id, username, password, email, alamat, nomor_telepon FROM users") 

    # Fetch hasil kueri masukkan ke var data
    data = cur.fetchall()

    # Tutup koneksi
    cur.close()

    # Render array data sebagai users bersama template
    return render_template('home.html', users=data)

# Endpoint untuk menambah user baru
@app.route('/add_user', methods=['POST'])
def add_user():
    # Ambil data dari permintaan
    data = request.get_json()
    username = data['username']
    password = data['password']
    email = data['email']
    alamat = data['alamat']
    nomor_telepon = data['nomor_telepon']

    # Cursor koneksi mysql
    cur = mysql.connection.cursor()

    # Insert kueri untuk menambah data baru
    cur.execute("INSERT INTO users (username, password, email, alamat, nomor_telepon) VALUES (%s, %s, %s, %s, %s)", 
                (username, password, email, alamat, nomor_telepon))

    # Commit perubahan
    mysql.connection.commit()

    # Tutup koneksi
    cur.close()

    return jsonify({'message': 'User added successfully'}), 200

# Endpoint untuk mengedit user
@app.route('/edit_user/<int:id>', methods=['PUT'])
def edit_user(id):
    # Ambil data dari permintaan
    data = request.get_json()
    username = data['username']
    password = data['password']
    email = data['email']
    alamat = data['alamat']
    nomor_telepon = data['nomor_telepon']

    # Cursor koneksi mysql
    cur = mysql.connection.cursor()

    # Update kueri
    cur.execute("UPDATE users SET username=%s, password=%s, email=%s, alamat=%s, nomor_telepon=%s WHERE id=%s",
                (username, password, email, alamat, nomor_telepon, id))

    # Commit perubahan
    mysql.connection.commit()

    # Tutup koneksi
    cur.close()

    return jsonify({'message': 'User updated successfully'}), 200

# Endpoint untuk menghapus user
@app.route('/delete_user/<int:id>', methods=['DELETE'])
def delete_user(id):
    # Cursor koneksi mysql
    cur = mysql.connection.cursor()

    # Delete kueri
    cur.execute("DELETE FROM users WHERE id=%s", (id,))

    # Commit perubahan
    mysql.connection.commit()

    # Tutup koneksi
    cur.close()

    return jsonify({'message': 'User deleted successfully'}), 200

# Debug dan auto reload
if __name__ == '__main__':
    app.run(debug=True)
