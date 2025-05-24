while True: 
    A1 = float(input("masukkan bilangan pertama: "))
    A2 = float(input("masukkan bilangan kedua: "))   
   
    print("pilih operasi yang kamu inginkan:")
    print("1. penjumlahan")
    print("2. pengurangan")
    print("3. perkalian")
    print("4. pembagian")
    print("5. keluar")

    pilihan = int(input("masukkan pilihanmu (ketik angkanya): "))

    if pilihan == 1:
        hasil =  A1+A2
        print(f'hasil penjumlahannya = {hasil}')
    elif pilihan == 2:
        hasil = A1-A2
        print(f'hasil pengurangannya = {hasil}')
    elif pilihan == 3:
        hasil = A1*A2
        print(f'hasil perkaliannya = {hasil}')
    elif pilihan == 4:
        if A2 == 0:
            print(f'error: pembagian dengan nol tidak diperbolehkan')
        else:
            hasil = A1/A2
            print (f'hasil pembagiannya = {hasil}')  
    else:
        print('thank you.')
        break

    lanjut_hitung = input("ulangi?(yes/no): ").lower()
    if lanjut_hitung == 'no' :
        print ('selesai')
        break
