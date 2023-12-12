# Определяем базовый класс Transport
class Transport():
    def __init__(self, coordinates, speed, brand, year, number):
        self._coordinates = coordinates
        self._speed = speed
        self._brand = brand
        self._year = year
        self._number = number
    
    # Создаем геттер и сеттер для координат
    @property
    def coordinates(self):
        return self._coordinates
 
    @coordinates.setter
    def coordinates(self, coordinates):
        self._coordinates = coordinates
    
    # Создаем геттер и сеттер для скорости
    @property
    def speed(self):
        return self._speed
 
    @speed.setter
    def speed(self, speed):
        if speed >= 0:
            self._speed = speed
 
    # Создаем геттер и сеттер для марки
    @property
    def brand(self):
        return self._brand
 
    @brand.setter
    def brand(self, brand):
        self._brand = brand

    # Создаем геттер и сеттер для года выпуска
    @property
    def year(self):
        return self._year
 
    @year.setter
    def year(self, year):
        if year >= 0:
            self._year = year

    # Создаем геттер и сеттер для номера
    @property
    def number(self):
        return self._number
 
    @number.setter
    def number(self, number):
        self._number = number
    
    # Переопределяем метод __str__ для вывода информации о транспорте
    def __str__(self):
        return f"Coordinates: {self.coordinates}, Speed: {self.speed}, Brand: {self.brand}, Year: {self.year}, Number: {self.number}"
 
    # Создаем метод для проверки присутствия транспортного средства в заданной области
    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        return pos_x <= self.coordinates[0] <= pos_x + length and pos_y <= self.coordinates[1] <= pos_y + width
 
# Определяем класс Passenger
class Passenger():
    def __init__(self, passengers_capacity, number_of_passengers):
        self._passengers_capacity = passengers_capacity
        self._number_of_passengers = number_of_passengers
    
    # Создаем геттер и сеттер для вместимости пассажиров
    @property
    def passengers_capacity(self):
        return self._passengers_capacity
 
    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if passengers_capacity >= 0:
            self._passengers_capacity = passengers_capacity

    # Создаем геттер и сеттер для количества пассажиров на борту
    @property
    def number_of_passengers(self):
        return self._number_of_passengers
 
    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if number_of_passengers >= 0:
            self._number_of_passengers = number_of_passengers
 
# Определяем класс Cargo
class Cargo():
    def __init__(self, carrying):
        self._carrying = carrying

    # Создаем геттер и сеттер для грузоподъемности
    @property
    def carrying(self):
        return self._carrying
 
    @carrying.setter
    def carrying(self, carrying):
        if carrying >= 0:
            self._carrying = carrying
 
# Определяем класс Plane, наследуя от Transport
class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self._height = height

    # Создаем геттер и сеттер для высоты полета
    @property
    def height(self):
        return self._height
 
    @height.setter
    def height(self, height):
        if height >= 0:
            self._height = height
 
# Определяем класс Auto, наследуя от Transport
class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)
 
# Определяем класс Ship, наследуя от Transport
class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self._port = port

    # Создаем геттер и сеттер для порта
    @property
    def port(self):
        return self._port
 
    @port.setter
    def port(self, port):
        self._port = port
 
# Определяем класс Car, наследуя от Auto
class Car(Auto):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)
 
# Определяем класс Bus, наследуя от Auto и Passenger
class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, passengers_capacity, number_of_passengers):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)
 
# Определяем класс CargoAuto, наследуя от Auto и Cargo
class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, carrying):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Cargo.__init__(self, carrying)
 
# Определяем класс Boat, наследуя от Ship
class Boat(Ship):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number, port)
 
# Определяем класс PassengerShip, наследуя от Ship и Passenger
class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, port, passengers_capacity, number_of_passengers):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)
 
# Определяем класс CargoShip, наследуя от Ship и Cargo 
class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, port, carrying):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Cargo.__init__(self, carrying)
 
# Определяем класс Airplane, наследуя от Plane
class Airplane(Plane):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number, height)
 
# Определяем класс PassengerPlane, наследуя от Plane и Passenger
class PassengerPlane(Plane, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, height, passengers_capacity, number_of_passengers):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)
 
# Определяем класс CargoPlane, наследуя от Plane и Cargo
class CargoPlane(Plane, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, height, carrying):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Cargo.__init__(self, carrying)
 
# Определяем класс Seaplane, наследуя от Plane и Ship
class Seaplane(Plane, Ship):
    def __init__(self, coordinates, speed, brand, year, number, height, port):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        
# Создаем объекты для проверки каждого класса

# Создаем объект класса Transport
transport = Transport([0, 0], 100, "Toyota", 2010, "ABC123")

# Создаем объект класса Passenger
passenger = Passenger(50, 30)

# Создаем объект класса Cargo
cargo = Cargo(5000)

# Создаем объект класса Plane
plane = Plane([1000, 1000], 500, "Boeing", 2015, "XYZ789", 10000)

# Создаем объект класса Auto
auto = Auto([500, 500], 80, "BMW", 2012, "DEF456")

# Создаем объект класса Ship
ship = Ship([2000, 2000], 200, "Titanic", 1912, "GHI789", "Southampton")

# Создаем объект класса Car
car = Car([100, 100], 60, "Ford", 2008, "JKL012")

# Создаем объект класса Bus
bus = Bus([300, 300], 70, "Mercedes", 2013, "MNO345", 40, 25)

# Создаем объект класса CargoAuto
cargoAuto = CargoAuto([800, 800], 90, "Volvo", 2016, "PQR678", 3000)

# Создаем экземпляр класса Boat
boat = Boat([30, 40], 30, "River", 2005, "BOAT01", "River Port")

# Создаем экземпляр класса PassengerShip
passenger_ship = PassengerShip([60, 60], 50, "Sea Ship", 2010, "PAS01", "Sea Port", 200, 150)

# Создаем объект класса CargoShip
cargo_ship = CargoShip([0, 0], 40, "CargoShip1", 2000, "EE7890", "London", 5000)

# Создаем объект класса Airplane
airplane = Airplane([0, 10], 700, "Boeing", 2018, "FF2345", 12000)

# Создаем объект класса PassengerPlane
passenger_plane = PassengerPlane([30, 30], 300, "PassengerPlaneBrand", 2010, "JKL012", 10000, 200, 150)

# Создаем объект класса CargoPlane
cargo_plane = CargoPlane([40, 40], 400, "CargoPlaneBrand", 2005, "MNO345", 15000, 5000)

# Создаем объект класса Seaplane
#seaplane = Seaplane([50, 50], 200, "SeaplaneBrand", 2015, "PQR678", 5000, "Port")
# Выводит: Coordinates: [50, 50], Speed: 200, Brand: SeaplaneBrand, Year: 2015, Number: PQR678

# Выводим информацию о каждом объекте
print(transport)
print(passenger)
print(cargo)
print(plane)
print(auto)
print(ship)
print(car)
print(bus)
print(cargoAuto)
print(boat)
print(passenger_ship)
print(cargo_ship)
print(airplane)
print(passenger_plane)
print(cargo_plane)
#print(seaplane)

"""
В данном решении мы создаем объекты для каждого класса и выводим информацию о каждом объекте с помощью переопределенного метода __str__ из класса Transport.
"""