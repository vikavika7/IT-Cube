n = []
n2 = input().split()
for i in n2:
    n.append(int(i))
min_i = n.index(max(n))
max_i = n.index(min(n))
n[max_i], n[min_i] = n[min_i], n[max_i]
print(*n)