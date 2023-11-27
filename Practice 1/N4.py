'''
## 문제 설명
정수 하나(n)를 입력 받아서 소수(prime)인지 판별하는 프로그램을 작성해보자. 단, 아래와 같은 예외처리를 추가한다.
- 입력된 정수가 0이거나 0보다 작은 값을 입력할 경우, “Only Positive!”라고 출력한다.
- 숫자가 아닌 문자열을 입력할 경우, “Wrong Input!”라고 출력한다.

## 입력 예시#1
3

## 출력 예시#1
Prime

## 입력 예시#2
12

## 출력 예시#2
Not Prime

## 입력 예시#3
-5

## 출력 예시#3
Only Positive!

## 입력 예시#4
Hello

## 출력 예시#4
Wrong Input!
'''
class Zero(Exception):
    def __str__(self):
        return "Only Positive!"

try:
    n = int(input())
    if n <= 0:
        raise Zero
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("Prime")
    else:
        print("Not Prime")

except Zero as e:
    print(e)

except Exception:
    print("Wrong Input!")
