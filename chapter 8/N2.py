class Time:
  def __init__(self, t):
    self.h = t // 3600
    self.m = t % 3600 // 60
    self.s = t % 60
  
  def print_info(self):
    print(f"Hour : {self.h}")
    print(f"Minute : {self.m}")
    print(f"Second : {self.s}")

t = int(input())
p1 = Time(t)
p1.print_info()
