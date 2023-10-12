numbers = input("Введите последовательность чисел через пробел: ")
print(any(numbers[i] == numbers[j] for i in range(len(numbers)) for j in range(i+1, len(numbers)) if numbers[i].isdigit() and numbers[j].isdigit()))





