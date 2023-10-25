a = int(input())
b = int(input())
c = int(input())

x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a

print(f"{x1:0.1f} / {x2:0.1f}")
