n = input()
r = list(n)
for i in range(len(r) // 2):
    temp = r[i]
    r[i] = r[len(r) - i - 1]
    r[len(r) - i - 1] = temp
#print(r)
sum = 0
for i in range(len(r)):
    if r[i] == '1':
        sum += 2 ** i
print(sum)
