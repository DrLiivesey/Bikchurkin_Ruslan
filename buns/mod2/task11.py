numbers = input("Введите последовательность чисел через пробел: ")
has_duplicates = False # Инициализировать переменную для проверки наличия одинаковых цифр
current_number = ""# Инициализировать переменную для текущего числа

for i in range(len(numbers)):
    if numbers[i].isdigit():
        current_number += numbers[i]
    if not numbers[i].isdigit() or i == len(numbers) - 1:  # Если символ - не цифра или это последний символ в строке
        for j in range(i+1, len(numbers)):  # Проход по оставшимся числам после текущего числа
            if numbers[j].isdigit() and current_number == numbers[j]:# Если найдены два одинаковых числа
                has_duplicates = True
                break
        current_number = ""
        
print(has_duplicates)