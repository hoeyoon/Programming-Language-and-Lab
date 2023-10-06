'''
## 문제 설명
사이트 주소와 비밀번호가 쌍으로 들어오는 데이터로부터 원하는 비밀번호를 출력하는 프로그램을 작성해보자.
- (입력) 첫째 줄에 저장된 사이트 주소의 수 N(1 ≤ N ≤ 1,000)과 비밀번호를 찾으려는 사이트 주소의 수 M(1 ≤ M ≤ 1,000)이 제공된다.
- 두 번째 줄부터 N개의 사이트 주소와 비밀번호가 주어지고, 이 두 개는 공백으로 구분한다.
- 사이트 주소는 알파벳 대소문자와 마침표로 이루어져 있으며, 비밀번호는 알파벳으로만 구성된다.
- (출력) M개의 줄에 걸쳐 해당 비밀번호를 차례대로 출력한다.

## 입력 예시
6 2						 
noj.am IU					 
acmicpc.net UAENA
startlink.io THEKINGOD
hanyang.ac.kr SOMEDAY
dhlottery.co.kr BOO
mcc.hanyang.ac.kr ADREAMER
startlink.io
acmicpc.net

## 출력 예시
THEKINGOD
UAENA
'''
n, m = map(int, input().split())
passwords = {}
for i in range(n):
  site, pw = input().split()
  passwords[site] = pw
for i in range(m):
  site = input()
  print(passwords[site])