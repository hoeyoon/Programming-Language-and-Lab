class Number:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def getMin(self):
    return min(self.x, self.y)
    
  def getMax(self):
    return max(self.x, self.y)

  def getGCD(self):
    a = self.getMax()
    b = self.getMin()
    while b > 0:
      a, b = b, a % b
    return a
  
  def getLCM(self):  
    return (self.x * self.y) // self.getGCD()



x, y = map(int, input().split())
number = Number(x, y)
print(f"Max Num : {number.getMax()}")
print(f"Min Num : {number.getMin()}")
print(f"GCD Num : {number.getGCD()}")
print(f"LCM Num : {number.getLCM()}")
