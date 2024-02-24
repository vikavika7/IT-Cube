n = input().split()
num = []
for j in n:
    if int(j) % 2 == 0:
        s = int(j) ** 2
        if s % 10 != 4:
            num.append(s)
print(*num)