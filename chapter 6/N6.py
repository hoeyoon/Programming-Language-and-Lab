'''
## 문제 설명
일주일에 해당하는 7개의 기온 정보(소수점)을 입력받고, 최저 기온을 찾아서 요일을 출력하는 프로그램을 작성해보자.
- 요일은 순서와 출력 형태는 다음과 같다.
- Mon, Tue, Wed, Thu, Fri, Sat, Sun 
- 대소문자를 구분하니 이에 유의하자!

## 입력 예시#1
18.0 19.0 20.0 21.0 22.0 23.0 24.0

## 출력 예시#1
Mon

## 입력 예시#2
21.5 22.2 19.4 18.5 21.7 22.8 24.0

## 출력 예시#2
Thu
'''
n = list(map(float, input().split()))
day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
a = min(n)
for i in range(len(n)):
  if a == n[i]:
    b = i
print(day[b])