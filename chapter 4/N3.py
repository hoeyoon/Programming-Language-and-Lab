h, w = map(int, input().split())
bmi = w / ((h / 100) * (h / 100))
if bmi > 35.0:
  print("Obesity Level 3")
elif bmi > 30.0:
  print("Obesity Level 2")
elif bmi > 25.0:
  print("Obesity Level 1")
elif bmi > 23.0:
  print("Over Weight")
elif bmi > 18.5:
  print("Normal")
else:
  print("Low Weight")