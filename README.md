# Sistem Data Pasien Rumah Sakit (CRUD - Python)

## Deskripsi Program
Program ini merupakan **aplikasi CRUD (Create, Read, Update, Delete)** berbasis **Python** yang digunakan untuk mengelola **data pasien rumah sakit**.  
Semua proses dilakukan melalui **terminal/command prompt**, dengan sistem **login admin** untuk menjaga keamanan data.

Program ini menggunakan:
- Collection data type (list dan dictionary)
- Conditional (`if`, `else`, `while`)
- Regular Function (`def`)
- Input/output text

---

## Fitur 
### 1. **Login Sistem**
Sebelum mengakses menu utama, pengguna harus login dengan memasukkan username dan password berikut:
- **Username:** `admin`
- **Password:** `12345`

Jika login berhasil, pengguna diarahkan ke menu utama.

---

### 2. **Menu Utama**
Setelah login, akan tampil menu:
```
1. Tampilkan Data Pasien
2. Tambah Data Pasien
3. Ubah Data Pasien
4. Hapus Data Pasien
5. Keluar
```
Pengguna dapat memilih menu sesuai kebutuhan dengan mengetik angka 1–5.

---

### 3. **Tampilkan Data Pasien**
Menampilkan seluruh data pasien yang tersimpan dalam format tabel sederhana:
```
ID       | Nama   | Umur | Diagnosa
-----------------------------------
RM-001   | Hafi   | 25   | Demam
RM-002   | Theo   | 30   | Flu
```
Jika belum ada data, sistem akan menampilkan pesan “Belum ada data pasien.”

---

### 4. **Tambah Data Pasien**
Fitur untuk menambahkan pasien baru.  
Sebelum mengisi data, pengguna bisa mengetik **'1'** untuk kembali ke menu utama tanpa menambah data.  

Program akan otomatis membuat **ID pasien baru** berdasarkan ID terakhir (contoh: dari RM-005 menjadi RM-006).

Input yang diminta:
- Nama pasien  
- Umur pasien  
- Diagnosa pasien  

Setelah data ditambahkan, sistem menampilkan pesan konfirmasi.

---

### 5. **Ubah Data Pasien**
Fitur untuk mengedit data pasien yang sudah ada.  
Langkah:
1. Menampilkan seluruh data pasien.  
2. Pengguna memasukkan **ID pasien** yang ingin diubah.  
3. Jika ditemukan, pengguna dapat mengganti nama, umur, atau diagnosa (kosongkan jika tidak ingin mengubah bagian tertentu).  

Contoh:
```
Masukkan ID pasien yang ingin diubah (contoh: RM-002): RM-003
Nama baru: hesa
Umur baru: 22
Diagnosa baru: flu
```
Jika ID tidak ditemukan, sistem akan menampilkan pesan “ID pasien tidak ditemukan.”

---

### 6. **Hapus Data Pasien**
Fitur untuk menghapus satu atau beberapa pasien sekaligus.  
Pengguna dapat memasukkan beberapa ID dengan koma, contoh:
```
RM-001, RM-003
```

Program akan menghitung berapa data yang berhasil dihapus dan menampilkan hasilnya.  
Jika tidak ada ID valid yang ditemukan, akan muncul pesan kesalahan.

Sebelum menghapus, pengguna juga dapat mengetik **'1'** untuk kembali ke menu utama.

---

### 7. **Keluar dari Program**
Memilih opsi **5** pada menu utama akan menghentikan program dengan menampilkan pesan “Program selesai.”

---

## Struktur dan Alur Program
1. Program dimulai dari fungsi **`login()`**
2. Setelah login berhasil → masuk ke **`menu_utama()`**
3. Dari menu utama, pengguna dapat mengakses fungsi:
   - `tampilkan_data()`
   - `tambah_pasien()`
   - `ubah_pasien()`
   - `hapus_pasien()`
4. Semua menu memiliki opsi untuk **kembali ke menu utama** tanpa melakukan perubahan data.
