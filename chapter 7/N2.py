'''
## 문제 설명
문자열을 하나 입력받아서 소문자는 대문자로, 대문자는 소문자로 변환하는 프로그램을 작성해보자.
- 문자열은 오로지 대문자와 소문자 알파벳으로만 구성된다.
- 공백과 특수문자 등은 입력되지 않는다.

## 입력 예시
Alphabet

## 출력 예시
aLPHABET
'''
a = input()
for i in a:
  if 'a' <= i <= 'z':
    print(i.upper(),end='')
  else:
    print(i.lower(), end='')