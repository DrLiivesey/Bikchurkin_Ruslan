domain = input("Введите доменное имя сайта: ")
result = []
start = len(domain)
for i in range(len(domain)-1, -1, -1): # Обратный проход по доменному имени
    if domain[i] == ".": # Если найден разделитель доменов
        result.append(domain[i+1:start]) # Добавить найденный домен в результат
        start = i# Обновить начальный индекс для следующего домена
result.append(domain[0:start])# Добавить последний домен в результат
for i in range(len(result)-1, -1, -1): # Вывести результат в обратном порядке
    print(result[i])