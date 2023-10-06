'''
## 문제 설명
N개의 정수를 입력받아서 입력받은 수들의 평균을 계산한다. 
입력받은 정수들 중에서 평균값과 가장 차이가 작은 정수의 인덱스를 출력한다. 
- 평균값은 소수점을 가질 수 있다.
- 만약 차이가 동일한 정수가 있다면 작은 인덱스를 출력한다.
- 예를 들어서, “2 1 3 5 4”가 입력된다면, 평균값은 3이 된다. 여기서, 입력된 정수와 차이는 “1 2 0 2 1”이 되고, 가장 차이가 작은 입력된 정수는 3이므로 해당 인덱스인 2를 출력한다.

## 입력 예시
2 1 3 5 4

## 출력 예시
2
'''
l1 = list(map(int, input().split()))
res = 0
for i in l1:
  res += i
res = res // len(l1)
for i in range(len(l1)):
  if l1[i] > res:
    l1[i] = l1[i] - res
  else:
    l1[i] = res - l1[i]
  #print(l1[i], end=' ')
index = 0
min = l1[0]
for i in range(len(l1)):
  if l1[i] < min:
    min = l1[i]
    index = i
print(index)