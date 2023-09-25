"""
## 문제 설명
지수함수 exp(x)의 테일러 급수(Taylor Series)는 아래와 같다. 
테일러 급수를 활용하여 지수함수를 계산하는 프로그램을 작성해보자. 
- 단, 함수를 활용하여 지수함수를 계산한다.
- 소수점 둘째자리까지 출력한다.
- 입력으로 x와 n값을 입력한다.
- exp(x) = sigma(x^n / n!) where n = [0부터 무한대]        
         = (x^0 / 0!) + (x^1 / 1!) + (x^2 / 2!) + (x^3 / 3!) + ...  


## 입력 예시#1
2 100

## 출력 예시#1
7.39

## 입력 예시#2
5 200

## 출력 예시#2
148.41
"""
def taylor(x, n):
  r = 0
  for i in range(n + 1):
    r += (x ** i) / fac(i)
  return r
def fac(a):
  sum = 1
  for i in range(1, a + 1):
    sum *= i
  return sum
x, n = map(int, input().split())
print("%.2f" %taylor(x, n))