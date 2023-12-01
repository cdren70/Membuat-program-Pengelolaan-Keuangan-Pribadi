import json

manajemen_keuangan = {
    "pengeluaran": [],
    "anggaran_awal": 0,
    "laporan_keuangan": {}
}

def simpan_data():
    with open("manajemen_keuangan.json", "w") as file:
        json.dump(manajemen_keuangan, file, indent=4)

def baca_data():
    try:
        with open("manajemen_keuangan.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return manajemen_keuangan

def tambah_pengeluaran():
    deskripsi = input("Masukkan deskripsi pengeluaran: ")
    jumlah = float(input("Masukkan jumlah pengeluaran: Rp "))
    manajemen_keuangan['pengeluaran'].append({"deskripsi": deskripsi, "jumlah": jumlah})
    simpan_data()

def anggaran_awal():
    anggaran = float(input("Masukkan jumlah anggaran: Rp"))
    manajemen_keuangan['anggaran_awal'] = anggaran
    simpan_data()

def laporan_keuangan():
    laporan = baca_data()
    print("Laporan Keuangan:")
    print("Pengeluaran:")
    for pengeluaran in laporan['pengeluaran']:
        print(f"Deskripsi: {pengeluaran['deskripsi']}, Jumlah: Rp {pengeluaran['jumlah']}")
    print(f"Anggaran Awal: Rp {laporan['anggaran_awal']}")
    print("=====================================")

def tampilkan_sisa_anggaran():
    laporan = baca_data()
    total_pengeluaran = sum(item['jumlah'] for item in laporan['pengeluaran'])
    anggaran = laporan['anggaran_awal']
    status_anggaran = anggaran - total_pengeluaran
    print(f"Total Pengeluaran: Rp {total_pengeluaran}")
    print(f"Sisa Anggaran: Rp {status_anggaran}")
    print("=====================================")

def main():
    while True:
        print("Pengelolaan Keuangan Pribadi by Kelompok 10")
        print("1. Anggaran Awal")
        print("2. Tambah Pengeluaran")
        print("3. Laporan Keuangan")
        print("4. Tampilkan Status Anggaran")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            anggaran_awal()
        elif pilihan == '2':
            tambah_pengeluaran()
        elif pilihan == '3':
            laporan_keuangan()
        elif pilihan == '4':
            tampilkan_sisa_anggaran()
        elif pilihan == '5':
            print("Terima Kasih Sudah Menggunakan App ini :)-Kelompok 10")
            break
        else:
            print("Pilihan tidak ada.")

if __name__ == "__main__":
    main()
