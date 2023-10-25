n = list(map(int, input().split()))
m = list(map(int, input().split()))
for i in m:
    if i in n:
        print(end="1 ")
    else:
        print(end="0 ")
