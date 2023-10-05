number = input('введите число ')
if not number.isdigit(): # Проверяем, является ли введенное значение целым числом
    print("Неверный ввод")
else:
    num = int(number)
    binary = ""
    octal = ""
    hexa = ""
    # Переводим в двоичную систему счисления
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    # Переводим в восьмеричную систему счисления
    num = int(number)
    while num > 0:
        octal = str(num % 8) + octal
        num //= 8
    # Переводим в шестнадцатеричную систему счисления
    num = int(number)
    while num > 0:
        ans = num % 16
        if ans < 10:
            hexa = str(ans) + hexa
        else:
            hexa = chr(ord('A') + ans - 10) + hexa
        num //= 16

    print(binary + ", " + octal + ", " + hexa)