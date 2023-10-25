n = int(input())
count = 0
s = [0] * (n + 1)
for i in range(2, n + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            s[i]+=1
for i in range(len(s)):
    if s[i] == 2:
        count += i

print(count)
