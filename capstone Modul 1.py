data_pasien = [
    {"id": "RM-001", "nama": "Hafi", "umur": 25, "diagnosa": "Demam"},
    {"id": "RM-002", "nama": "Theo", "umur": 30, "diagnosa": "Flu"},
    {"id": "RM-003", "nama": "Udin", "umur": 21, "diagnosa": "Sakit Kepala"},
    {"id": "RM-004", "nama": "Aca", "umur": 24, "diagnosa": "Batuk"},
    {"id": "RM-005", "nama": "Adit", "umur": 50, "diagnosa": "Tipes"},
]

# Fungsi login
def login():
    print("=== LOGIN SISTEM DATA PASIEN ===")
    username_benar = "admin"
    password_benar = "12345"

    while True:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username == username_benar and password == password_benar:
            print("Login berhasil.")
            menu_utama()
            break
        else:
            print("Username atau Password salah, coba lagi.\n")

# Fungsi utama (menu sistem)
def menu_utama():
    while True:
        print("\n=== SISTEM DATA PASIEN RUMAH SAKIT ===")
        print("1. Tampilkan Data Pasien")
        print("2. Tambah Data Pasien")
        print("3. Ubah Data Pasien")
        print("4. Hapus Data Pasien")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            tambah_pasien()
        elif pilihan == "3":
            ubah_pasien()
        elif pilihan == "4":
            hapus_pasien()
        elif pilihan == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Fungsi menampilkan data pasien
def tampilkan_data():
    print("\n=== DAFTAR DATA PASIEN ===")
    if len(data_pasien) == 0:
        print("Belum ada data pasien.")
    else:
        print("ID\t | Nama\t | Umur\t | Diagnosa")
        print("--------------------------------------")
        i = 0
        while i < len(data_pasien):
            pasien = data_pasien[i]
            print(f"{pasien['id']}\t | {pasien['nama']}\t | {pasien['umur']}\t | {pasien['diagnosa']}")
            i += 1
    input("\nTekan Enter untuk kembali ke menu utama.")

def tampilkan_data2():
    print("\n=== DAFTAR DATA PASIEN ===")
    if len(data_pasien) == 0:
        print("Belum ada data pasien.")
    else:
        print("ID\t | Nama\t | Umur\t | Diagnosa")
        print("--------------------------------------")
        i = 0
        while i < len(data_pasien):
            pasien = data_pasien[i]
            print(f"{pasien['id']}\t | {pasien['nama']}\t | {pasien['umur']}\t | {pasien['diagnosa']}")
            i += 1
 
# Fungsi menambah data pasien
def tambah_pasien():
    print("\n=== TAMBAH DATA PASIEN ===")
    kembali = input("Ketik '1' untuk kembali ke menu utama atau tekan Enter untuk lanjut: ")
    if kembali == "1":
        return

    # Ambil ID terakhir
    if len(data_pasien) == 0:
        id_baru = "RM-001"
    else:
        id_terakhir = data_pasien[-1]["id"] 
        nomor_terakhir = int(id_terakhir.split("-")[1])
        id_baru = f"RM-{nomor_terakhir + 1:03d}"
    nama = input("Masukkan nama pasien: ").title()
    umur = int(input("Masukkan umur pasien: "))
    diagnosa = input("Masukkan diagnosa pasien: ").title()

    data_pasien.append({"id": id_baru, "nama": nama, "umur": umur, "diagnosa": diagnosa})
    print("Data pasien berhasil ditambahkan.")
    input("\nTekan Enter untuk kembali ke menu utama.")

# Fungsi mengubah data pasien
def ubah_pasien():
    print("\n=== UBAH DATA PASIEN ===")
    kembali = input("Ketik '1' untuk kembali ke menu utama atau tekan Enter untuk lanjut: ")
    if kembali == "1":
        return

    tampilkan_data2()
    id_edit = input("\nMasukkan ID pasien yang ingin diubah (contoh: RM-001): ").upper()
    if id_edit == "1":
        return

    found = False
    i = 0
    while i < len(data_pasien):
        if data_pasien[i]["id"] == id_edit:
            print("Masukkan data baru (kosongkan jika tidak ingin mengubah):")
            nama_baru = input("Nama baru: ").title()
            umur_baru = input("Umur baru: ")
            diagnosa_baru = input("Diagnosa baru: ").title()

            if nama_baru != "":
                data_pasien[i]["nama"] = nama_baru
            if umur_baru != "":
                data_pasien[i]["umur"] = int(umur_baru)
            if diagnosa_baru != "":
                data_pasien[i]["diagnosa"] = diagnosa_baru

            print("Data pasien berhasil diubah.")
            found = True
            break
        i += 1

    if not found:
        print("ID pasien tidak ditemukan.")
    input("\nTekan Enter untuk kembali ke menu utama.")

# Fungsi menghapus data pasien (bisa lebih dari satu ID)
def hapus_pasien():
    print("\n=== HAPUS DATA PASIEN ===")
    kembali = input("Ketik '1' untuk kembali ke menu utama atau tekan Enter untuk lanjut: ")
    if kembali == "1":
        return

    tampilkan_data2()
    ids_input = input("\nMasukkan ID pasien yang ingin dihapus (pisahkan dengan koma, contoh: RM-001,RM-003): ")

    if ids_input == "1":
        return

    ids_hapus = []
    for bagian in ids_input.split(","):
        bagian = bagian.strip().upper()
        if bagian.startswith("RM-"):
            ids_hapus.append(bagian)

    if len(ids_hapus) == 0:
        print("Tidak ada ID valid yang dimasukkan.")
        input("\nTekan Enter untuk kembali ke menu utama.")
        return

    jumlah_awal = len(data_pasien)
    i = 0
    while i < len(data_pasien):
        if data_pasien[i]["id"] in ids_hapus:
            del data_pasien[i]
        else:
            i += 1

    jumlah_akhir = len(data_pasien)
    terhapus = jumlah_awal - jumlah_akhir

    if terhapus > 0:
        print(f"{terhapus} data pasien berhasil dihapus.")
    else:
        print("Tidak ada ID yang cocok untuk dihapus.")
    input("\nTekan Enter untuk kembali ke menu utama.")

# Jalankan program
login()