# transchive
A store-transaction archiving system

### Alur Kerja

0. Wait until begin transaction
1. Barcode reading
2. Parsing barcode definition
   2.1 from Input manual
   2.2 from Input from scanner
3. ​Update database
4. Write data to transaction's bill
5. While not end of transaction, repeat from 1
6. Print transaction's bill
7. Repeat from 0.

### Field database

#### Barang
---------
* barcode
* nama barang
* stok
* harga

#### Barcode
---------
* barcode
* nama barang

#### Transaksi
---------
* trx_id
* kode transaksi
* kode barang
* qty
* total
