a = int(input("Number a : "))
b = int(input("Number b : "))
c = int(input("Number c : "))
s1 = ((-b + ((b ** 2) - 4 * a * c) ** 0.5)) / 2 * a
s2 = ((-b - ((b ** 2) - 4 * a * c) ** 0.5)) / 2 * a
print("Solution : %.1f, %.1f" % (s1, s2))