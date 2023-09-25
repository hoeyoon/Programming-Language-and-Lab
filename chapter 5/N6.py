"""
## 문제 설명
조합(combination)의 경우 팩토리얼(factorial)를 활용하여 계산 가능하다. 
팩토리얼을 활용하여 조합을 계산해보자.
- nCr = n! / ((n-r)! * r!)
- 조합과 팩토리얼은 함수로 작성해보자.
- 함수 예시:
	def combination(n, r)
	def factorial(x)


## 입력 예시#1
5 3

## 출력 예시#1
10

## 입력 예시#2
12 5

## 출력 예시#2
792
"""
def com(n, r):
  r = fac(n) / (fac(n - r) * fac(r))
  return r
def fac(x):
  sum = 1
  for i in range(1, x + 1):
    sum *= i
  return sum
n, r = map(int, input().split())
print("%d" %com(n, r))