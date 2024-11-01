# config.py
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sidakaton",  # Ganti dengan password MySQL Anda
        database="app_penjualan"
    )
