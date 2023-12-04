# Импортировать модули requests и json.
import requests
import json

# Загрузить данные с API Star Wars по кораблю с id=10 и преобразовать их в формат json.
data = json.loads(requests.get('https://swapi.dev/api/starships/10').text)

# Создать пустой список pilots
pilots = []

# список заполним информацией по каждому пилоту:
for pilot in data['pilots']:
    # Загрузить информацию о пилоте по ссылке и преобразовать ее в формат json
    pilot_info_all = json.loads(requests.get(pilot).text)

    # Создать словарь pilot_info,
    # содержащий информацию о пилоте:
    # имя, рост, масса, родная планета и ссылка на информацию о родной планете.

    pilot_info = {'name': pilot_info_all['name'],  # имя пилота
                  'height': pilot_info_all['height'],  # рост пилота
                  'mass': pilot_info_all['mass'],  # масса пилота
                  'homeworld': json.loads(requests.get(pilot_info_all['homeworld']).text)['name'],
                  # родная планета пилота
                  'homeworld_url': pilot_info_all['homeworld']}  # ссылка на информацию о родной планете пилота
    # Добавить словарь pilot_info в список pilots.
    pilots.append(pilot_info)

# Создать словарь new_data, содержащий информацию о корабле:
# название, максимальную скорость, класс и список пилотов.
new_data = {'name': data['name'],  # название корабля
            'max_atmosphering_speed': data['max_atmosphering_speed'],  # максимальная скорость
            'starship_class': data['starship_class'],  # класс
            'pilots': pilots}  # список пилотов

# Открыть файл info_starship.json для записи в формате json с отступами в 4 пробела.
with open('info_starship.json', 'w') as file:
    # Записать словарь new_data в файл.
    json.dump(new_data, file, indent=4)

# Вывести на экран данные new_data в формате json с отступами в 4 пробела.
print(json.dumps(new_data, indent=4))