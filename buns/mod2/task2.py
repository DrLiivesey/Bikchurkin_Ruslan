side = float(input("Введите длину стороны квадрата: ")) # Получаем длину стороны квадрата от пользователя
perimeter = 4 * side # Рассчитываем периметр, площадь и диагональ
area = side ** 2
diagonal = (2 * side ** 2) ** 0.5

print("Периметр квадрата: {:.2f}".format(perimeter))
print("Площадь квадрата: {:.2f}".format(area))
print("Диагональ квадрата: {:.2f}".format(diagonal))