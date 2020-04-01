a = int(input())
b = ''

if a == 0:
    b = '0' + b
    
while a > 0:
    if a % 2 > 0:
        b = '1' + b
    else:
        b = '0' + b
    a = a // 2

print(b)
