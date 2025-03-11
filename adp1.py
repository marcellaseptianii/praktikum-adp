print('===== Menu Paket Makanan ======')
print("Ayam = Rp20.000")
print("Sapi = Rp35.000")
print("Cumi Cumi = Rp45.000")

paket = str(input("Masukkan Menu (Ayam/Sapi/Cumi): ")).lower().strip()
if paket == "ayam" :
    harga = 20000
elif paket == "sapi" :
    harga = 35000
else :
    harga = 45000

jarak = float(input("Masukkan jarak rumah anda ke restoran (dalam km): "))
if jarak<1 :
    ongkir = 0
elif 1<=jarak<=3:
    ongkir = 7000
else:
    ongkir = 15000

total_biaya = harga+ongkir
print(f"Total yg perlu anda bayar adalah: Rp{total_biaya:,}") 