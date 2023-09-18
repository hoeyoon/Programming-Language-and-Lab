n = int(input())
a, b, r = 1, 1, 1
for i in range(2, n + 1):
  r = a + b
  a, b = b, r
print(r)