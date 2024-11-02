
<p align="center">
    <img src="https://github.com/user-attachments/assets/54c78825-9680-475f-a2cc-e4c4eaebf8fb" alt="Foto Anda" style="width: 500px; height: auto;">
</p>

<h1>Aplikasi Kelola Barang</h1>

<p>Aplikasi ini adalah sebuah sistem berbasis web menggunakan <strong>Flask</strong> dan <strong>MySQL</strong> untuk mengelola data barang masuk. Aplikasi mencakup fitur <strong>CRUD</strong> dan tampilan statistik barang masuk secara harian dan bulanan.</p>

<h2>Fitur</h2>
<ul>
    <li><strong>CRUD Produk:</strong> Menambah, mengedit, menghapus, dan menampilkan daftar produk.</li>
    <li><strong>Statistik Barang Masuk:</strong> Menampilkan total barang masuk harian, bulanan, dan grafik mingguan.</li>
    <li><strong>Tampilan Responsif:</strong> Menggunakan template HTML responsif dan ramah pengguna.</li>
</ul>

<h2>Persyaratan</h2>
<ul style="list-style-type: none; padding: 0;">
    <li style="display: flex; align-items: center; margin-bottom: 10px;">
        <img src="https://www.python.org/static/img/python-logo@2x.png" alt="Python Logo" style="width: 80px; height: auto; margin-right: 10px;">
        <span style="flex: 1;">3.12.1 atau di atasnya</span>
    </li>
    <li style="display: flex; align-items: center; margin-bottom: 10px;">
        <img src="https://www.mysql.com/common/logos/logo-mysql-170x115.png" alt="MySQL Logo" style="width: 40px; height: auto; margin-right: 10px;">
        <span style="flex: 1;">MySQL</span>
    </li>
    <li style="display: flex; align-items: center; margin-bottom: 10px;">
        <img src="https://th.bing.com/th?id=ODLS.d766d530-29c4-4ac0-baec-2097804c4549&w=32&h=32&qlt=90&pcl=fffffa&o=6&pid=1.2" alt="Virtualenv Logo" style="width: 17px; height: auto; margin-right: 10px;">
        <span style="flex: 1;">Virtualenv</span>
    </li>
</ul>
<h2>Instalasi</h2>

<h3>1. Clone Repositori</h3>
<pre><code>git clone https://github.com/username/nama-repositori.git
cd nama-repositori</code></pre>

<h3>2. Buat dan Aktifkan Virtual Environment</h3>
<pre><code>python -m venv myenv</code></pre>
<p>Aktifkan virtual environment:</p>
<ul>
    <li><strong>Windows:</strong> <code>myenv\Scripts\activate</code></li>
    <li><strong>MacOS/Linux:</strong> <code>source myenv/bin/activate</code></li>
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
<pre><code>python app.py  ATAU  flask run</code></pre>

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
    <li><strong> ⚠️ Jika Tetap Error:</strong> Coba introspeksi diri anda .</li>
</ul>

<h2>Menonaktifkan Virtual Environment</h2>
<p>Nonaktifkan virtual environment dengan:</p>
<pre><code>deactivate</code></pre>

<h2>Lisensi</h2>
<p>Proyek ini dilisensikan di bawah <a href="LICENSE">MIT License</a>.</p>

<a href="https://github.com/ZidanAlfianMubarok/Pemrograman-Web-Praktikum" class="button">Lihat Repositori di GitHub</a>

</body>
</html>
