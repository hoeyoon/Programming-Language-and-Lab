a, b, c = map(int, input().split())
sum = 0
if a + b > c:
  sum += 1
if a + c > b:
  sum += 1
if b + c > a:
  sum += 1
if sum == 3:
  print("Triangle O")
else:
  print("Triangle X")