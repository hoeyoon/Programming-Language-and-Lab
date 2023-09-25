"""
## 문제 설명
정수 하나를 입력받아서 해당 정수가 소수(prime)인지 아닌지를 판별하는 프로그램을 작성해보자. 
- 단, 함수를 활용하여 소수(prime)인지를 판별한다.


## 입력 예시#1
5

## 출력 예시#1
Prime

## 입력 예시#2
9

## 출력 예시#2
Not Prime
"""
def prime_check(a):
  count = 0
  for i in range(1, a + 1):
    if a % i == 0:
      count += 1
  if count == 2:
    return 1
  else:
    return 0
a = int(input())
if prime_check(a) == 1:
  print("Prime")
else:
  print("Not Prime")