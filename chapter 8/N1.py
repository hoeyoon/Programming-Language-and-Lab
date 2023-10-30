class Person:
  def __init__(self, h, w):
    self.h = h
    self.w = w
    bmi = w / ((h / 100) ** 2)
    self.bmi = bmi
  
  def print_info(self):
    print(f"Height : {self.h} cm")
    print(f"Weight : {self.w} kg")
    print(f"BMI : {self.bmi:0.2f}")

h, w = map(int, input().split())
p1 = Person(h, w)
p1.print_info()
