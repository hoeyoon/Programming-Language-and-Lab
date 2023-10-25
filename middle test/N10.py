n = input()
s = [0] * 26
for i in n:
    if i.isalpha() == 1:
        s[ord(i) - ord('a')] += 1

print(*s)
