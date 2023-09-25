"""
## 문제 설명
초(second)를 입력 받아서 시간(hour), 분(minute), 초(second)의 단위로 출력하는 프로그램을 작성해보자.

## 입력 예시
Number : 10000

## 출력 예시
Hour : 2
Minute : 46
second : 40
"""

s = int(input("Number : "))
sec = s % 60
hour = s / 3600
min = (s % 3600)/60
print("Hour : %d" % hour)
print("Minute : %d" % min)
print("Second :", sec)
