n = input()
for i in n:
    if i.isalpha() == 1:
        if 'a' <= i <= 'z':
            print(i.upper(), end="")
        else:
            print(i.lower(), end="")
