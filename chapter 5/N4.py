"""
## 문제 설명
피보나치(Fibonacci) 수열이 있다. 
입력된 정수로부터 해당 인덱스에 해당하는 피보나치 수열의 값을 출력하는 프로그램을 작성해보자.
- 피보나치 수열 : f(x) = f(x-1) + f(x-2)
- f(0) = 0, f(1) = 1
- 단, 순환호출을 하는 재귀함수를 활용하자.


## 입력 예시#1
5

## 출력 예시#1
5

## 입력 예시#2
10

## 출력 예시#2
55
"""
def fib(a):
  if a == 0:
    return 0
  elif a == 1:
    return 1
  else:
    return fib(a - 1) + fib(a - 2)
a = int(input())
print(fib(a))