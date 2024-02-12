a = int(input())
a1 = a // 100
b = a % 10
c = (a  // 10) % 10
d = (a1 + b + c) - min(a1, b, c) - max(a1,b, c)
if (max(a1, b, c) - min(a1, b, c)) == d:
    print('прикольное')
else:
    print('не прикольное')