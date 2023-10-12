n = input("Введите число: ")
result = f"{int(n):b}, {int(n):o}, {int(n):X}" if n.isdigit() else "Неверный ввод"
print(result)