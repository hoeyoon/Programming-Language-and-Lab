L = int(input())
ai = list(map(int, input().split()))
r = []
for i in range(len(ai)):
  s = max(0, i - L // 2)
  e = min(len(ai), i + L // 2 + 1)
  r.append(min(ai[s:e]))
print(*r)