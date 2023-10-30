'''
## 문제 설명
2개의 정수를 입력받아 최소값/최대값/최대공약수/최소공배수를 구하는 프로그램을 작성해보자.
- 최소값, 최대값, 최대공약수, 최소공배수를 구하는 메소드(멤버 함수)를 구현한다.
- 강의자료에 있는 코드를 활용하여 클래스 기반으로 작성한다.

- 최대공약수는 유클리드 호제법을 통하여 구현한다.
1) 큰 수에서 작은 수로 나머지 연산(%)을 수행
2) 작은 수와 1번을 통하여 나온 결과와 나머지 연산(%)을 수행
3) 1-2를 반복적으로 수행하다가, 나머지가 0이 되면 그 때의 작은 수가 최대공약수이다.

- 최소공배수는 아래와 같이 구현 가능하다.
* 입력받은 두 수의 곱을 최대공약수로 나눈다.

## 입력 예시 
12 6

## 출력 예시
Max Num : 12
Min Num : 6
GCD Num : 6
LCM Num : 12
'''
class Number:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def getMin(self):
    return min(self.x, self.y)
    
  def getMax(self):
    return max(self.x, self.y)

  def getGCD(self):
    a = self.getMax()
    b = self.getMin()
    while b > 0:
      a, b = b, a % b
    return a
  
  def getLCM(self):  
    return (self.x * self.y) // self.getGCD()

x, y = map(int, input().split())
number = Number(x, y)
print(f"Max Num : {number.getMax()}")
print(f"Min Num : {number.getMin()}")
print(f"GCD Num : {number.getGCD()}")
print(f"LCM Num : {number.getLCM()}")
