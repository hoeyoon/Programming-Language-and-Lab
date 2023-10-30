'''
## 문제 설명
한 학생의 이름과 국어, 영어, 수학, 과학 점수를 차례대로 입력받는다. 학생의 총점과 평균을 구하는 프로그램을 작성해보자.
- 총점과 평균을 구하는 메소드(멤버 함수)를 구현한다.
- 강의자료에 있는 코드를 활용하여 클래스 기반으로 작성한다.

## 입력 예시 :
Hong Gil Dong	# 이름 입력
100 90 80 70	# 점수 순서대로 입력

## 출력 예시 :
[Hong Gil Dong] Total : 340, Average : 85.0
'''
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
    avg = self.k + self.e + self.m + self.s
    return avg

  def getAvgScore(self):
    return self.getTotalScore() / 4

name = input()
k, e, m, s = map(int, input().split())
a = Student(name, k, e, m, s)
print(f"[{a.getName()}] Total : {a.getTotalScore()},", end=" ")
print(f"Average : {a.getAvgScore():.1f}")
