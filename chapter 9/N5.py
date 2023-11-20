'''
## 문제 설명
월(month)와 일(day)를 가리키는 2개의 정수를 입력받아 아래와 같은 형태로 출력하는 프로그램을 작성해보자.
- 2월은 28일로 계산한다.
- 1월에서 12월 사이가 아니면, “Wrong Month!”라고 출력해보자.
- 해당 월에 존재하는 일(day)가 아니면 “Wrong Day!”라고 출력해보자.
- 사용자 정의 에러를 활용해보자.

입력예시#1 : 
1 30		

출력예시#1 : 
January 30

입력예시#2 : 
12 20		

출력예시#2 : 
December 20

입력예시#3 : 
2 30		

출력예시#3 : 
Wrong Day!

입력예시#4 : 
13 10		

출력예시#4 : 
Wrong Month!
'''
class MonthError(Exception):
  def __str__(self):
    return "Wrong Month!"

class DayError(Exception):
  def __str__(self):
    return "Wrong Day!"

def day_of_month(m, d):
  if m == 2:
    if d > 28 or d < 1:
      raise DayError
    return d
  days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  return days_in_month[m - 1]

try:
  month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  m, d = map(int, input().split())
  if m < 1 or m > 12:
    raise MonthError
  if d > day_of_month(m, d) or d < 1:
    raise DayError
  print(f"{month[m - 1]} {d}")

except DayError as e1:
  print(e1)

except MonthError as e2:
  print(e2)