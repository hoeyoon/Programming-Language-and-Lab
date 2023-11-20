'''
## 문제 설명
신장(cm)과 몸무게(kg)를 입력 받아서 체질량지수(BMI)를 계산하는 프로그램을 작성해보자.
- BMI 지수 = 몸무게(kg) / (신장(m) x 신장(m))
- 잘못된 입력을 받을 경우, “Wrong Input!”을 출력하도록 하자.

입력예시#1 : 
170 70		

출력예시#1 : 
24.22

입력예시#2 : 
170 70 60	

출력예시#2 : 
Wrong Input!

입력예시#3 : 
170 	
	
출력예시#3 : 
Wrong Input!

입력예시#4 : 
Hello 70	

출력예시#4 : 
Wrong Input!
'''
try:
  h, w = map(int, input().split())
  bmi = w / ((h / 100) ** 2)
  print(f"{bmi:0.2f}")

except Exception:
  print("Wrong Input!")