import os

# Dictionary untuk menyimpan data mahasiswa
data_mahasiswa = {}

def tambah_data():
    os.system("clear")  # Membersihkan layar (gunakan "cls" untuk Windows)
    print("Tambah Data")
    nim = input("NIM: ")
    nama = input("Nama: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    data_mahasiswa[nim] = {"nama": nama, "tugas": tugas, "uts": uts, "uas": uas, "akhir": nilai_akhir}
    print("Data berhasil ditambahkan!")

def ubah_data():
    os.system("clear")
    print("Ubah Data")
    nim = input("Masukkan NIM yang akan diubah: ")
    if nim in data_mahasiswa:
        nama = input("Nama baru: ")
        tugas = float(input("Nilai Tugas baru: "))
        uts = float(input("Nilai UTS baru: "))
        uas = float(input("Nilai UAS baru: "))
        nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
        data_mahasiswa[nim] = {"nama": nama, "tugas": tugas, "uts": uts, "uas": uas, "akhir": nilai_akhir}
        print("Data berhasil diubah!")
    else:
        print("Data dengan NIM tersebut tidak ditemukan!")

def hapus_data():
    os.system("clear")
    print("Hapus Data")
    nim = input("Masukkan NIM yang akan dihapus: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print("Data berhasil dihapus!")
    else:
        print("Data dengan NIM tersebut tidak ditemukan!")

def tampilkan_data():
    os.system("clear")
    print("Daftar Nilai Mahasiswa")
    print("="*80)
    print("| NO |    NIM    |     NAMA     | TUGAS | UTS | UAS | NILAI AKHIR |")
    print("="*80)
    if data_mahasiswa:
        for i, (nim, data) in enumerate(data_mahasiswa.items(), start=1):
            print(f"| {i:<2} | {nim:<9} | {data['nama']:<12} | {data['tugas']:<5} | {data['uts']:<3} | {data['uas']:<3} | {data['akhir']:<11.2f} |")
    else:
        print("|                          TIDAK ADA DATA                          |")
    print("="*80)

def cari_data():
    os.system("clear")
    print("Cari Data")
    nim = input("Masukkan NIM yang dicari: ")
    if nim in data_mahasiswa:
        data = data_mahasiswa[nim]
        print("Data ditemukan!")
        print(f"NIM: {nim}")
        print(f"Nama: {data['nama']}")
        print(f"Nilai Tugas: {data['tugas']}")
        print(f"Nilai UTS: {data['uts']}")
        print(f"Nilai UAS: {data['uas']}")
        print(f"Nilai Akhir: {data['akhir']:.2f}")
    else:
        print("Data dengan NIM tersebut tidak ditemukan!")

def menu():
    while True:
        print("\nProgram Input Nilai")
        print("===================")
        print("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar")
        pilihan = input("Pilih menu: ").lower()

        if pilihan == "l":
            tampilkan_data()
        elif pilihan == "t":
            tambah_data()
        elif pilihan == "u":
            ubah_data()
        elif pilihan == "h":
            hapus_data()
        elif pilihan == "c":
            cari_data()
        elif pilihan == "k":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
menu()
