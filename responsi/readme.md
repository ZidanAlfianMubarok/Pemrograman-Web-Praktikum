<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Aplikasi Statistik Barang Masuk</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #0056b3;
        }
        h1 {
            font-size: 2em;
            text-align: center;
        }
        h2, h3 {
            border-bottom: 2px solid #0056b3;
            padding-bottom: 5px;
            margin-top: 1.5em;
        }
        p, li {
            line-height: 1.6;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            background-color: #eee;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: Consolas, 'Courier New', monospace;
            color: #d63384;
        }
        ul, ol {
            padding-left: 20px;
        }
        .button {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            font-size: 1em;
            color: #fff;
            background-color: #0056b3;
            border-radius: 5px;
            text-decoration: none;
        }
        .button:hover {
            background-color: #003366;
        }
    </style>
</head>
<body>

<h1>Aplikasi Statistik Barang Masuk</h1>

<p>Aplikasi ini adalah sebuah sistem berbasis web menggunakan <strong>Flask</strong> dan <strong>MySQL</strong> untuk mengelola data barang masuk. Aplikasi mencakup fitur <strong>CRUD</strong> dan tampilan statistik barang masuk secara harian dan bulanan.</p>

<h2>Fitur</h2>
<ul>
    <li><strong>CRUD Produk:</strong> Menambah, mengedit, menghapus, dan menampilkan daftar produk.</li>
    <li><strong>Statistik Barang Masuk:</strong> Menampilkan total barang masuk harian, bulanan, dan grafik mingguan.</li>
    <li><strong>Tampilan Responsif:</strong> Menggunakan template HTML responsif dan ramah pengguna.</li>
</ul>

<h2>Persyaratan</h2>
<ul>
    <li>Python 3.x</li>
    <li>MySQL</li>
    <li>Virtualenv</li>
</ul>

<h2>Instalasi</h2>

<h3>1. Clone Repositori</h3>
<pre><code>git clone https://github.com/username/nama-repositori.git
cd nama-repositori</code></pre>

<h3>2. Buat dan Aktifkan Virtual Environment</h3>
<pre><code>python -m venv venv</code></pre>
<p>Aktifkan virtual environment:</p>
<ul>
    <li><strong>Windows:</strong> <code>venv\Scripts\activate</code></li>
    <li><strong>MacOS/Linux:</strong> <code>source venv/bin/activate</code></li>
</ul>

<h3>3. Instal Dependensi</h3>
<pre><code>pip install Flask mysql-connector-python</code></pre>

<h3>4. Konfigurasi Database</h3>
<p>Buat database MySQL dengan nama <code>app_penjualan</code>:</p>
<pre><code>CREATE DATABASE app_penjualan;
USE app_penjualan;
CREATE TABLE tb_produk (
    kode_barang VARCHAR(20) PRIMARY KEY,
    nama_barang VARCHAR(100),
    harga DECIMAL(10, 2),
    stok INT,
    kd_supplier VARCHAR(20),
    created_at DATE
);</code></pre>

<h3>5. Konfigurasi Koneksi Database</h3>
<p>Atur kredensial MySQL di file <code>config.py</code> sesuai dengan konfigurasi MySQL Anda:</p>
<pre><code>def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password_anda",
        database="app_penjualan"
    )</code></pre>

<h3>6. Menjalankan Aplikasi</h3>
<p>Jalankan aplikasi Flask dengan perintah berikut:</p>
<pre><code>python app.py</code></pre>

<p>Aplikasi akan berjalan di <a href="http://127.0.0.1:5000" target="_blank">http://127.0.0.1:5000</a>.</p>

<h2>Struktur Direktori</h2>
<p>Struktur direktori untuk proyek ini:</p>
<pre><code>project_directory/
├── app.py                # File utama aplikasi Flask
├── config.py             # Konfigurasi database
├── templates/            # Direktori template HTML
│   ├── index.html
│   ├── statistik.html
│   ├── update.html
│   └── about.html
├── static/               # Folder file statis (CSS, JS, dll.)
└── venv/                 # Virtual environment</code></pre>

<h2>Endpoints</h2>
<ul>
    <li><code>/</code>: Menampilkan daftar produk.</li>
    <li><code>/create</code>: Menambah produk baru.</li>
    <li><code>/update/&lt;kode_barang&gt;</code>: Mengedit produk.</li>
    <li><code>/delete/&lt;kode_barang&gt;</code>: Menghapus produk.</li>
    <li><code>/statistik</code>: Menampilkan statistik barang masuk.</li>
    <li><code>/about</code>: Menampilkan halaman tentang aplikasi.</li>
</ul>

<h2>Troubleshooting</h2>
<ul>
    <li><strong>Koneksi Database Gagal:</strong> Periksa kredensial MySQL di <code>config.py</code> dan pastikan server MySQL aktif.</li>
    <li><strong>Error Lainnya:</strong> Pastikan semua dependensi terinstal di virtual environment yang aktif.</li>
</ul>

<h2>Menonaktifkan Virtual Environment</h2>
<p>Nonaktifkan virtual environment dengan:</p>
<pre><code>deactivate</code></pre>

<h2>Lisensi</h2>
<p>Proyek ini dilisensikan di bawah <a href="LICENSE">MIT License</a>.</p>

<a href="https://github.com/username/nama-repositori" class="button">Lihat Repositori di GitHub</a>

</body>
</html>