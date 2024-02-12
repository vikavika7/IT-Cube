num=int(input())
total=0
while num != 0:
    last_digit = num % 10
    if last_digit < 1:
        total += 1
    num //= 10
print(total) 