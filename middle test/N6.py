def square_sum(n):
    sum = 0
    for i in n:
        sum += i ** 2
    return sum

n = list(map(int, input().split()))
print(square_sum(n))
