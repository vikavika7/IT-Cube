num=int(input())
while num != 0:
    last_digit = num % 10
    if last_digit == 2:
        break
    num //= 100
print(last_digit)