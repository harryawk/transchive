import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# def create_test_table():
#     cursor.execute('CREATE TABLE IF NOT EXISTS testTable_(id INT, nama VARCHAR, stok INT)')

# def fill_test_table():
#     cursor.execute('INSERT INTO testTable_ VALUES(99, "hello", 11)')
#     conn.commit()
# def fetching_data():
# 	cursor.execute("SELECT * FROM testTable_")
# 	print cursor.fetchall()[0][1]
# 	conn.commit()

cursor.execute('CREATE TABLE IF NOT EXISTS stok(id INT, nama_barang VARCHAR, stok INT, harga INT)')	
cursor.execute('CREATE TABLE IF NOT EXISTS barcode(id INT, nama_barang VARCHAR, barcode VARCHAR)')	
cursor.execute('CREATE TABLE IF NOT EXISTS transaksi(id INT, id_trx INT, nama_barang VARCHAR, jumlah INT, total_harga INT, tanggal DATE)')	

# create_test_table()
# fill_test_table()
# fetching_data()
cursor.close()
conn.close()