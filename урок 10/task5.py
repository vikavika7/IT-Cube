a ='w w w o r l d g g g g r e a t t e c c h e m g g p w w'
n = 0
n2 = []
for i in range(2, len(a), 2):
    if a[i] != a[i-2]:
        n2.append(a[n:i].split)
        n = i
n2.append(a[n:].split)
print(n2)