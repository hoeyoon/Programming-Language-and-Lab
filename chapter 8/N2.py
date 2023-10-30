'''
## 문제 설명
초(second)를 입력받아서 시간(hour), 분(minute), 초(second)의 단위로 출력하는 프로그램을 작성해보자.
- 강의자료에 있는 코드를 활용하여 클래스 기반으로 작성한다.

## 입력 예시 :
10000

## 출력 예시 :
Hour : 2
Minute : 46
Second : 40
'''
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
