'''
## 문제 설명
N개의 정수를 입력받아서 최대값에서 최소값을 뺀 결과를 출력하는 프로그램을 작성해보자.
- 여기서 N의 범위는, 1 ≤ N ≤ 1000

## 입출력 예시
입력#1 : 100 200 300		출력#1 : 200
입력#2 : 100 200		출력#2 : 100
입력#2 : 4 3 2 1 5 6 7 8	출력#3 : 7
'''
l1 = list(map(int, input().split()))
print(max(l1) - min(l1))