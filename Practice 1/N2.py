'''
## 문제 설명
슬라이딩 윈도우의 사이즈(L)와 N개의 정수(Ai)를 입력받아 윈도우 안에서의 최소값을 찾는 프로그램을 작성해보자.
- 예를 들어서, 아래와 같은 입력을 가정해보자. 	3
	1 2 3 4 5 6 7 8 
- 슬라이딩 윈도우의 사이즈는 3이고, 8개의 정수를 입력받았다. 
- 0번째 인덱스를 기준으로 크기가 3인 윈도우를 씌우면, “- 1 2”가 해당되므로, 최소값은 1이 된다. 
- 1번째 인덱스를 기준으로 크기가 3인 윈도우를 씌우면, “1 2 3”이 해당되므로, 최소값은 1이 된다.
- 2번째 인덱스를 기준으로 크기가 3인 윈도우를 씌우면, “2 3 4”가 해당되므로, 최소값은 2가 된다.
- -10^9 ≤ Ai ≤ 10^9,  1 ≤ N ≤ 1000
- L은 항상 홀수이며, 1 ≤ L ≤ 99


## 입력 예시#1
3
1 2 3 4 5 6 7 8

## 출력 예시#1
1 1 2 3 4 5 6 7

## 입력 예시#2
5
1 1 1 1 1 2 2 2 2 2

## 출력 예시#2
1 1 1 1 1 1 1 2 2 2

## 입력 예시#3
5
5 4 3 2 1 1 2 3 4 5

## 출력 예시#3
3 2 1 1 1 1 1 1 2 3
'''
l = int(input())
l1 = list(map(int, input().split()))

r = []
for i in range(len(l1)):
    s = max(0, i - l // 2)
    e = min(len(l1), i + l // 2 + 1)
    r.append(min(l1[s:e]))

print(*r)
