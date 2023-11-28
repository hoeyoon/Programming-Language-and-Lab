'''
## 문제 설명
N개의 정수를 입력받아서 “좋은 수”의 개수를 구하는 프로그램을 작성해보자.
- N의 범위는, 1 ≤ N ≤ 1000.
- “좋은 수”는 입력 받은 정수 중에서 두 수의 합을 통하여 표현되는 수
- 예를 들어서, “2 1 3 5 4”를 입력한다면, 3은 1과 2의 합으로, 4는 1과 3의 합으로, 5는 4와 1의 합으로 표현되므로 좋은 수의 개수는 3이다.
- 자기 자신은 좋은 수 만들기에 포함해서는 안된다.

## 입출력 예시
입력#1 : 1 2 3			출력#1 : 1
입력#2 : 1 2 5			출력#2 : 0
입력#3 : 2 1 3 5 4	출력#3 : 3
'''
n = list(map(int, input().split()))
count = 0
l = len(n)
sum = set()
for i in range(l):
  for j in range(1 + i, l):
    sum.add(n[i] + n[j])
for i in n:
  if i in sum:
    count += 1
print(count)

#또는

def goodnum(n, num, x):
  for i in range(x):
    for j in range(i + 1, x):
      if num[i] + num[j] == n:
        return 1

  return 0

n = list(map(int, input().split()))
count = 0
for i in range(len(n)):
  if goodnum(n[i], n, len(n)):
    count += 1

print(count)
