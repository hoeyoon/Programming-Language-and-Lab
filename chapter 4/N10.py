"""
## 문제 설명
아래와 같은 출력이 나오는 코드를 작성해보자.
중첩 for문을 써서 코드를 작성하자.

## 출력 예시
    *
   ***
  *****
 *******
********* 
"""

for i in range(5):
  for j in range(4 - i):
    print(" ", end="")
  for j in range(i * 2 + 1):
    print("*", end="")
  print("\n", end="")
