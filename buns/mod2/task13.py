code = input('Введите код ')
odd_sum = 0 #переменная будет использоваться для хранения суммы нечетных цифр кода.
even_sum = 0
for i in range(len(code)):
    if i % 2 == 0: #так как отсчет начинается с нуля: четное становится нечетным и наоборот
        even_sum += int(code[i]) * 3
    else:
        odd_sum += int(code[i])
if (odd_sum + even_sum) % 10 == 0:
    print("yes")
else:
    print("no")