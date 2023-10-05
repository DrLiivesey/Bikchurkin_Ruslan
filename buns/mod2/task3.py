nums = input("Введите три целых числа через пробел: ")
a = ''
b = ''
c = ''
space = 0
for i in nums:
    if i == ' ':
        space += 1
    elif space == 0:
        a += i
    elif space == 1:
        b += i
    else:
        c += i
a = int(a)
b = int(b)
c = int(c)

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print(b)