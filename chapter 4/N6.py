"""
## 문제 설명
국어, 수학, 영어, 과학 점수를 입력 받아서 평균 점수를 계산한다.
평균 점수가 90점 이상인 경우 장학금을 받을 수 있다고 출력하는 프로그램을 작성해보자.

## 입력 예시 1
90 90 90 90

## 출력 예시 1
90.0 Scholarship O

## 입력 예시 2
90 90 89 89

## 출력 예시 2
89.5 Scholarship X
"""

a, b, c, d = map(int, input().split())
r = (a + b + c + d) / 4
if r >= 90:
  print("Scholarship O")
else:
  print("Scholarship X")
