class Student:
  def __init__(self, name, k, e, m, s):
    self.name = name
    self.k = k
    self.e = e
    self.m = m
    self.s = s

  def getName(self):
    return self.name

  def getTotalScore(self):
    self.avg = self.k + self.e + self.m + self.s
    return self.avg
  
  def getAvgScore(self):
    return self.avg / 4

name = input()
k, e, m, s = map(int, input().split())
a = Student(name, k, e, m, s)
print(f"[{a.getName()}] Total : {a.getTotalScore()},", end=" ")
print(f"Average : {a.getAvgScore():.1f}")
