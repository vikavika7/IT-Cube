n = input().split()
for i in range(len(n)):
    n[i] = int(n[i])
    n.sort()
    n.reverse()
print(*n)