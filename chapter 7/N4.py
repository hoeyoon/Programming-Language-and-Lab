'''
## 문제 설명
문자열을 하나 입력받아서 단어의 첫 글자를 모두 대문자로 나머지는 소문자로 변환하는 프로그램을 작성해보자.
- 입력되는 문자열은 대문자, 소문자, 공백만을 포함한다.

## 입력 예시 
LIFE is too sHORT

## 출력 예시
Life Is Too Short
'''
a = input()
a1 = a.split()
for i in a1:
  print(i.capitalize(), end = ' ')