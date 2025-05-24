n = int(input("input n: "))
jumlah_boom = 0
if n<4:
    print("n harus minimal 4.")
else:
    for i in range(n):
        for j in range(n):
            if n%2 == 1 and i == j == n//2:
                print(" HORE", end=" ")
            elif i==j :
                print("  1  ", end=" ")
            elif i + j == n-1:
                print ("  2  ", end=" ")
            else :
                print (" BOOM", end=" ")
                jumlah_boom += 1
        print ()

    print(f"total BOOM yang muncul sebanyak: {jumlah_boom}")
