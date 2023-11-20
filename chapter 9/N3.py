'''
## 문제 설명
신장(cm)과 몸무게(kg)를 입력 받아서 체질량지수(BMI)를 계산하는 프로그램을 작성해보자.
- BMI 지수 = 몸무게(kg) / (신장(m) x 신장(m))
- 신장과 몸무게에 0보다 작은 값을 입력할 경우, “Wrong Input!”을 출력하자.
- 그 이외의 잘못된 입력을 받을 경우, “Value Error!”을 출력하도록 하자.

입력예시#1 : 
170 70		

출력예시#1 : 
24.22

입력예시#2 : 
170 70 60	

출력예시#2 : 
Value Error!

입력예시#3 : 
Hello 70		

출력예시#3 : 
Value Error!

입력예시#4 : 
170 -70		

출력예시#4 : 
Wrong Input!
'''
try:
  a, b = map(int, input().split())
  if a > b:
    res = a // b
  else:
    res = b // a
  print(res)
except ZeroDivisionError:
  print("ZeroDivisionError")
except ValueError:
  print("ValueError")