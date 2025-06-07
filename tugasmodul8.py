# 10 data-data praktikan
data_pratikan = [
    ("2410432019", "Cella", 100, 97, 100),
    ("2410431021", "Chelsea", 60, 87, 95),
    ("2410433002", "Khanaya", 88, 95, 85),
    ("2410431013", "Tiara", 80, 64, 70),
    ("2410432029", "Ciya", 85, 73, 75),
    ("2410432009", "Nayla", 70, 80, 60),
    ("2410431041", "Ika", 55, 70, 88),
    ("2410433012", "Dwi", 85, 60, 80),
    ("24104331027", "Pujhi", 95, 60, 88),
    ("2410431033", "Marcel", 100, 94, 88)
]

# menyimpan ke file
with open("data_pratikan.txt", "w") as file:
    for data in data_pratikan:
        nim, nama, pretest, postest, tugas = data
        file.write(f"{nim},{nama},{pretest},{postest},{tugas}\n")

# membaca dan menyimpan ke dictionary
praktikan = {}
with open("data_pratikan.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        nim = data[0]
        nama = data[1]
        pretest = int(data[2])
        postest = int(data[3])
        tugas = int(data[4])

        praktikan[nim] = {
            "nama": nama,
            "pretest": pretest,
            "postest": postest,
            "tugas": tugas
        }

# menghitung nilai akhir dan menulis ke file
with open("data_nilai_akhir.txt", "w") as file:
    file.write(" NIM , Nama , Pretest , Postest , Tugas , Nilai Akhir\n")
    for nim, data in praktikan.items():
        nilai_akhir = (0.35 * data["pretest"] + 0.35 * data["postest"] + 0.30 * data["tugas"])
        nilai_akhir = float(f"{nilai_akhir:.2f}")
        data["nilai_akhir"] = nilai_akhir
        file.write(f"{nim},{data['nama']},{data['pretest']},{data['postest']},{data['tugas']},{nilai_akhir}\n")

# Membaca nilai akhir dari dictionary
nilai_akhir_list = []  
for nim, data in praktikan.items():
    nilai_akhir = data["nilai_akhir"]  
    nilai_akhir_list.append(nilai_akhir)

#nilai tertinggi & terendah
praktikan_tertinggi = None
praktikan_terendah = None

for nim, data in praktikan.items():
    if praktikan_tertinggi is None:
        praktikan_tertinggi = (nim, data)
    elif data["nilai_akhir"] > praktikan_tertinggi[1]["nilai_akhir"]:
        praktikan_tertinggi = (nim, data)

    if praktikan_terendah is None:
         praktikan_terendah = (nim, data)
    elif data["nilai_akhir"] < praktikan_terendah[1]["nilai_akhir"]:
        praktikan_terendah = (nim, data)

#rata-rata nilai akhir
rata_rata = sum(nilai_akhir_list) / len(nilai_akhir_list)
rata_rata = float(f"{rata_rata:.2f}")

#jmlh praktikan dgn nilai di bawah rata-rata
jumlah_bawah_rata = 0 

for nim, data in praktikan.items():
    if data["nilai_akhir"] < rata_rata:
        jumlah_bawah_rata += 1

#output
print('-------- Data Nilai Akhir Praktikan --------')    
print(f"Nilai tertinggi: {praktikan_tertinggi[1]['nama']} ({praktikan_tertinggi[0]}) = {praktikan_tertinggi[1]['nilai_akhir']}")
print(f"Nilai terendah: {praktikan_terendah[1]['nama']} ({praktikan_terendah[0]}) = {praktikan_terendah[1]['nilai_akhir']}")
print(f"Rata-rata nilai akhir: {rata_rata}")
print(f"Jumlah praktikan dengan nilai di bawah rata-rata: {jumlah_bawah_rata}")
