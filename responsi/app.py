from flask import Flask, render_template, request, redirect, url_for
from config import get_db_connection
from datetime import datetime

app = Flask(__name__)

# Rute Statistik Barang Masuk
@app.route('/statistik')
def statistik():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Hitung jumlah barang masuk hari ini
    cursor.execute("""
        SELECT COUNT(*) AS total_hari_ini
        FROM tb_produk
        WHERE DATE(created_at) = CURDATE()
    """)
    total_hari_ini = cursor.fetchone()["total_hari_ini"]

    # Hitung jumlah barang masuk bulan ini
    cursor.execute("""
        SELECT COUNT(*) AS total_bulan_ini
        FROM tb_produk
        WHERE MONTH(created_at) = MONTH(CURDATE()) AND YEAR(created_at) = YEAR(CURDATE())
    """)
    total_bulan_ini = cursor.fetchone()["total_bulan_ini"]

    # Ambil data jumlah barang masuk per hari selama 7 hari terakhir
    cursor.execute("""
        SELECT DATE(created_at) AS entry_date, COUNT(*) AS total_entries
        FROM tb_produk
        WHERE created_at >= CURDATE() - INTERVAL 6 DAY
        GROUP BY entry_date
        ORDER BY entry_date
    """)
    entries = cursor.fetchall()

    # Siapkan data untuk chart
    labels = [entry['entry_date'].strftime('%Y-%m-%d') for entry in entries]
    data = [entry['total_entries'] for entry in entries]

    cursor.close()
    conn.close()

    return render_template('statistik.html', total_hari_ini=total_hari_ini, total_bulan_ini=total_bulan_ini, labels=labels, data=data)

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tb_produk")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', products=products)

@app.route('/create', methods=['POST'])
def create():
    kode_barang = request.form['kode_barang']
    nama_barang = request.form['nama_barang']
    harga = request.form['harga']
    stok = request.form['stok']
    kd_supplier = request.form['kd_supplier']
    created_at = request.form['created_at']  # Ambil tanggal dari form

    # Konversi tanggal ke format yang sesuai jika diperlukan
    created_at_datetime = datetime.strptime(created_at, '%Y-%m-%d')

    # Simpan data ke database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tb_produk (kode_barang, nama_barang, harga, stok, kd_supplier, created_at) VALUES (%s, %s, %s, %s, %s, %s)",
        (kode_barang, nama_barang, harga, stok, kd_supplier, created_at_datetime)
    )
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('index', success=1)) # Tambahkan parameter `success=1`


@app.route('/update/<kode_barang>', methods=['GET', 'POST'])
def update(kode_barang):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        nama_barang = request.form['nama_barang']
        harga = request.form['harga']
        stok = request.form['stok']
        kd_supplier = request.form['kd_supplier']
        cursor.execute("""
            UPDATE tb_produk 
            SET nama_barang = %s, harga = %s, stok = %s, kd_supplier = %s 
            WHERE kode_barang = %s
        """, (nama_barang, harga, stok, kd_supplier, kode_barang))
        conn.commit()
        return redirect(url_for('index'))
    
    cursor.execute("SELECT * FROM tb_produk WHERE kode_barang = %s", (kode_barang,))
    product = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('update.html', product=product)

@app.route('/delete/<kode_barang>', methods=['POST'])
def delete(kode_barang):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tb_produk WHERE kode_barang = %s", (kode_barang,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))
# Rute untuk halaman About
@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(debug=True)
