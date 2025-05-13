x = [i for i in range(-7,8)]
n = len(x)
fx_list = []
for i in range(n):
    if x[i] > 0:
        fx = x[i]**3 - x[i]
    elif x[i] < 0:
        fx = 1 / (x[i]**2)
    else:
        fx = 1
    fx_list.append(fx)

print("| x  |   f(x)    |")
print("|----|-----------|")

for i in range(n):
    print(f"| {x[i]:>2} | {fx_list[i]:>9.4f} |")
