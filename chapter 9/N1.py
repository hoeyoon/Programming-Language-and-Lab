try:
  h, w = map(int, input().split())
  bmi = w / ((h / 100) ** 2)
  print(f"{bmi:0.2f}")

except Exception:
  print("Wrong Input!")