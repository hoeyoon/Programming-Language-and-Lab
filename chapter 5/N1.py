"""
## 문제 설명
실수형으로 섭씨온도를 입력받아서 화씨온도로 변환하는 프로그램을 작성해보자. 단, 함수(function)을 활용하여 작성해보자.
- F = (C * 1.8) + 32.0
- C : 섭씨온도, F : 화씨온도
- 소수점 둘째자리까지 출력한다.


## 입력 예시
28.0

## 출력 예시
82.40
"""
def temp(c):
  f = (c * 1.8) + 32.0
  return f
c = float(input())
print("%.2f" %temp(c))