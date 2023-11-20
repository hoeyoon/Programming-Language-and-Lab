def gcd(a, b):
  if a < b:
    a, b = b, a
  while b:
      a, b = b, a % b
  return a
  1
try:
  a, b = map(int, input().split())
  if a <= 0 or b <= 0:
    raise ValueError
  print(gcd(a, b))
  
except Exception:
  print("Wrong Input!")