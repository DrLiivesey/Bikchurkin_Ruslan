s = input("Введите строку: ")
vowels = 0
consonants = 0
for char in s:
    if char in "аеёоуыэюя":
        vowels += 1
    elif char.isalpha():
        consonants += 1
print(vowels,consonants)