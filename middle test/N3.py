n = int(input())
if n % 400 == 0 or n % 100 != 0 and n % 4 == 0:
    print("Leap Year O")
else:
    print("Leap Year X")
