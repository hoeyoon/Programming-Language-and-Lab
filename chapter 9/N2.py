'''
## 문제 설명
2개의 정수를 입력받아 최대공약수를 구하는 프로그램을 작성하자.
유클리드 호제법을 통하여 최대공약수를 계산한다.
- 큰 수에서 작은 수로 나머지 연산(%)을 수행
- 작은 수와 1번을 통하여 나온 결과와 나머지 연산(%)을 수행
- 1-2를 반복적으로 수행하다가, 나머지가 0이 되면 작은 수가 최대 공약수이다.
* 잘못된 입력이 나오면 “Wrong Input!”를 출력하도록 한다.

입력예시#1 : 
15 5		

출력예시#1 : 
5

입력예시#2 : 
15 0		

출력예시#2 : 
Wrong Input!

입력예시#3 : 
Hello 0		

출력예시#3 : 
Wrong Input!

입력예시#4 : 
15 5 5		

출력예시#4 : 
Wrong Input!
'''
def gcd(a, b):
  if a < b:
    a, b = b, a
  while b:
      a, b = b, a % b
  return a
  1
try:
  a, b = map(int, input().split())
  if a <= 0 or b <= 0:
    raise ValueError
  print(gcd(a, b))
  
except Exception:
  print("Wrong Input!")