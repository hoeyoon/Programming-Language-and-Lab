"""
## 문제 설명
여행비용을 계산하는 프로그램을 작성해보자
여행이 몇 박인지와 항공권의 가격, 호텔 1박 가격, 하루에 필요한 용돈을 입력 받아서 여행비용을 계산한다.
여행비용 = 항공권 가격 + 숙박일수 * 호텔 1박 가격 + (숙박일수 + 1) * 하루에 필요한 용돈

## 입력 예시
Flight : 1000000
Night : 3
Hotel : 200000
Allowance : 100000

## 출력 예시
Cost : 2000000
"""

f = int(input("Flight : "))
n = int(input("Night : "))
h = int(input("Hotel : "))
a = int(input("Allowance : "))
print("Cost : %d" % (f + n * h + (n + 1) * a))
