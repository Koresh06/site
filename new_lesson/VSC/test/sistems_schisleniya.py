a = int(input())
count = 0
while a != 0:
    num = a % 10
    if a > 2:
        count += num
    a = a // 10
print(count)