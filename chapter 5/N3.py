"""
## 문제 설명
초(second)를 입력받아서 시간(hour), 분(minute), 초(second)의 단위로 출력하는 프로그램을 작성해보자.
- 단, 함수를 활용해보자.
- 하나의 함수를 활용해서 시간, 분, 초 순서대로 반환값(return)을 설정해보자.


## 입력 예시 
10000

## 출력 예시
2 46 40
"""
def hms(a):
  h = a // 3600
  m = a % 3600 / 60
  s = a % 60
  return h, m, s
a = int(input())
print("%d %d %d" %hms(a))