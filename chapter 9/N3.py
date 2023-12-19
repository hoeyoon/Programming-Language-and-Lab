'''
## 문제 설명
2개의 정수를 입력받아 큰 수를 작은 수로 나눠서 몫을 구하는
프로그램을 작성하자.
1개 혹은 3개 이상의 정수를 입력받을 경우 “ValueError”라고 출력한다.
정수가 아닌 다른 자료형을 입력하면 “ValueError”라고 출력한다.
작은 수가 0일 경우 “ZeroDivisionError”라고 출력한다.

입력예시#1 : 4 15 

출력예시#1 : 3

입력예시#2 : 15 0 

출력예시#2 : ZeroDivisionError

입력예시#3 : 15 5 5 

출력예시#3 : ValueError

입력예시#4 : Hello 5 

출력예시#4 : ValueError
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
