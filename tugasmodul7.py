def menu():
    print("Menu:")
    print("1. Tabel perkalian modulo n")
    print("2. Mencari nilai sigma (Σx)")
    print("3. Mencari nilai faktorial n")
    print("4. Total dan rata-rata suatu data")
    print("5. Keluar")

def tabel_modulo():
    while True:
        n = int(input("Masukkan nilai n dari 1 sampai 10): "))
        if 1 <= n <= 10:
            break
        print("Ulangi, n harus antara 1 dan 10.")

    print("\n   |", end="")
    for i in range(n):
        print(f"{i:3}", end="")
    print("\n" + "-" * (n * 3 + 4))

    for i in range(n):
        print(f"{i:2} |", end="")
        for j in range(n):
            print(f"{(i*j) % n :3}", end="")
        print()

def sigma_x():
    while True:
        a = int(input("Batas atas: "))
        b = int(input("Batas bawah: "))
        if a >= b:
            break
        print("batas atas harus lebih besar atau sama dengan batas bawah.")

    total = 0
    for i in range(b, a + 1):
        total = total + i
    print("Σ x =", total)

def faktorial():
    while True:
        n = int(input("masukkan nilai n: "))
        if n >= 0:
            break
        print("ulangi, n harus besar dari 0: ")

    hasil = 1
    for i in range(1, n + 1):
        hasil = hasil*i
    print(f"{n}! =", hasil)

def total_ratarata():
    while True:
        jumlah = int(input("Masukkan banyak data: "))
        if jumlah > 0:
            break
        print("Ulangi, jumlah harus > 0:")

    data = []
    for i in range(jumlah):
        nilai = float(input(f"Data ke-{i+1}: "))
        data.append(nilai)

    total = 0
    for nilai in data:
        total = total + nilai

    rata = total / jumlah
    print("Total =", total)
    print("Rata-rata =", rata)


def pilihan():
    while True:
        menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tabel_modulo()
        elif pilihan == "2":
            sigma_x()
        elif pilihan == "3":
            faktorial()
        elif pilihan == "4":
            total_ratarata()
        elif pilihan == "5":
            print("Program telah selesai.")
            break
        else:
            print("Mohon ulangi, Pilihan tidak valid.")

pilihan()
