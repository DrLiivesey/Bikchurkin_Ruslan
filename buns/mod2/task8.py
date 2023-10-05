letters = input("Введите строку и символ через запятую: ")
s = ""
i = ""
comma = False
for char in letters:
    if char == "," and not comma: # Если символ - запятая и это первая встречанная запятая
        comma = True #запятая встречена
    elif comma:
        i += char
    else:
        s += char # Если запятая еще не встречалась, то символ добавляется в переменную s
count = 0
for j in range(len(s)):
    if s[j] == i and j == count:# Если найден символ i и он находится в начале строки
        count += 1
    else: # Если найден другой символ или символ i не находится в начале строки
        break

print(count)