"""
## 문제 설명
1부터 1000까지 모두 더하는 프로그램을 작성해보자. 공식을 활용하지 않고, for문과 while문을 활용하여 각각 작성해보자.

## 출력 예시 1
500500
"""

sum = 0
for i in range(1, 1001):
  sum += i
print(sum)

sum = 0
i = 1
while i <= 1000:
  sum += i
  i += 1
print(sum)
