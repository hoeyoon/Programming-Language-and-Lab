"""
## 문제 설명
신장(cm)과 몸무게(kg)를 입력 받아서 체질량지수(BMI)를 계산하는 프로그램을 작성해보자.
BMI 지수 = 몸무게(kg) / (신장(m) x 신장(m))

## 입력 예시
Height(cm) : 170
Weight(kg) : 70

## 출력 예시
BMI : 24.22
"""

h = int(input("Height(cm) : "))
w = int(input("Weight(kg) : "))
print("BMI : %.2f" % (w / (h/100 * h/100)))
