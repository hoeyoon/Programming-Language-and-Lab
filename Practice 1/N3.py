'''
## 문제 설명
2개의 정수를 입력받아 최소값/최대값/최대공약수/최소공배수를 구하는 프로그램을 작성한다.
- 두 개의 클래스가 존재한다. (SuperNumber, SubNumber)
- SubNumber 클래스는 SuperNumber 클래스를 상속받는다.
- SuperNumber 클래스에는 최소값, 최대값, 최대공약수를 구하는 메소드(멤버 함수)를 가진다.
- SubNumber 클래스는 최소공배수만을 구하는 메소드(멤버 함수)만을 가진다.
- SuperNumber 클래스만을 구현하여 코드를 완성하고, 이를 준수하지 않을 경우 시스템에서 정답이 나와도 오답으로 간주한다.
- SubNumber 클래스와 메인 모듈은 아래의 코드를 복사해서 사용하고, 수정하지 않는다.

class SubNumber(SuperNumber):
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def getLCM(self):
    return int(self.x * self.y / self.getGCD())

x, y = map(int, input().split())
number = SubNumber(x, y)
print(f"Max Num : {number.getMax()}")
print(f"Min Num : {number.getMin()}")
print(f"GCD Num : {number.getGCD()}")
print(f"LCM Num : {number.getLCM()}")

- 최대공약수는 유클리드 호제법을 통하여 구현한다.
1) 큰 수에서 작은 수로 나머지 연산(%)을 수행
2) 작은 수와 1번을 통하여 나온 결과와 나머지 연산(%)을 수행
3) 1-2를 반복적으로 수행하다가, 나머지가 0이 되면 그 때의 작은 수가 최대공약수이다.

## 입력 예시 
12 6

## 출력 예시
Max Num : 12
Min Num : 6
GCD Num : 6
LCM Num : 12
'''
class SuperNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getMax(self):
        return max(self.x, self.y)

    def getMin(self):
        return min(self.x, self.y)
    
    def getGCD(self):
        a = self.getMax()
        b = self.getMin()
        while b > 0:
            a, b = b, a % b
        return a
            
            

class SubNumber(SuperNumber):
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def getLCM(self):
    return int(self.x * self.y / self.getGCD())

x, y = map(int, input().split())
number = SubNumber(x, y)
print(f"Max Num : {number.getMax()}")
print(f"Min Num : {number.getMin()}")
print(f"GCD Num : {number.getGCD()}")
print(f"LCM Num : {number.getLCM()}")
