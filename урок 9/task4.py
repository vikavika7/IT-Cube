n = int(input())
a = []
for i in range(n):
    a.append(input())
b = int(input())
for i in a:
    if b <= len(i):
        print(i[b - 1], end='')