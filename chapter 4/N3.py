"""
## 문제 설명
신장(cm)과 몸무게(kg)를 입력 받아서 체질량지수(BMI)를 계산하고 비만도를 출력하는 프로그램을 작성해보자.
BMI 지수 = 몸무게(kg) / (신장(m) x 신장(m))
BMI ≤ 18.5  저체중
18.5 < BMI ≤ 23.0 -> 정상
23.0 < BMI ≤ 25.0 -> 과체중
25.0 < BMI ≤ 30.0 -> 비만1단계
30.0 < BMI ≤ 35.0 -> 비만2단계
35.0 < BMI -> 비만3단계

## 입력 예시
170 70

## 출력 예시
Over Weight
"""

h, w = map(int, input().split())
bmi = w / ((h / 100) * (h / 100))
if bmi > 35.0:
  print("Obesity Level 3")
elif bmi > 30.0:
  print("Obesity Level 2")
elif bmi > 25.0:
  print("Obesity Level 1")
elif bmi > 23.0:
  print("Over Weight")
elif bmi > 18.5:
  print("Normal")
else:
  print("Low Weight")
