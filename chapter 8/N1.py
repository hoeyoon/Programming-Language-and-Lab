'''
## 문제 설명
신장(cm), 몸무게(kg) 정보를 입력받아서 체질량지수(BMI)를 계산하는 프로그램을 작성해보자.
- BMI 지수 = 몸무게(kg) / (신장(m) x 신장(m))
- 강의자료에 있는 코드를 활용하여 클래스 기반으로 작성한다.

## 입력예시 : 
170 70

## 출력예시 : 
Height : 170 cm
Weight : 70 kg
BMI : 24.22
'''
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
