n = list(map(int, input().split()))
count = 0
l = len(n)
sum = set()
for i in range(l):
  for j in range(1 + i, l):
    sum.add(n[i] + n[j])
for i in n:
  if i in sum:
    count += 1
print(count)