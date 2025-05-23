titik = []
for i in range(3):
    x = float(input(f"Masukkan x untuk titik ke-{i+1}: "))
    y = float(input(f"Masukkan y untuk titik ke-{i+1}: "))
    titik.append([x, y])

A = ((titik[1][0] - titik[0][0])**2 + (titik[1][1] - titik[0][1])**2)**0.5
B = ((titik[2][0] - titik[1][0])**2 + (titik[2][1] - titik[1][1])**2)**0.5
C = ((titik[2][0] - titik[0][0])**2 + (titik[2][1] - titik[0][1])**2)**0.5

if A == B or B == C or A == C:
    print("ketiga titik membentuk segitiga sama kaki.")
else:
    print("ketiga titik tidak membentuk segitiga sama kaki.")
