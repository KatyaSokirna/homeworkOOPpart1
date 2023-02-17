# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, произво-
# дителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реа-
# лизуйте доступ к отдельным полям через методы класса.
class Car:
    name = 'Volkswagen Tiguan'
    year_of_production = '2017'
    machine_manufacturer = 'Volkswagen AG'
    engine_capacity = '2'
    color = 'grey'
    cost = '15000'

    def car_name(self):
        return self.name

    def change_car_name(self, new_car_name):
        self.name = new_car_name

    def car_year_of_production(self):
        return self.year_of_production

    def change_car_year_of_production(self, new_car_year_of_production):
        self.year_of_production = new_car_year_of_production

    def show_manufacturer(self):
        return self.machine_manufacturer

    def change_manufacturer(self, new_manufacturer):
        self.machine_manufacturer = new_manufacturer

    def show_capacity(self):
        return self.engine_capacity

    def change_capacity(self, new_capacity):
        self.engine_capacity = new_capacity

    def show_color(self):
        return self.color

    def change_color(self, new_color):
        self.color = new_color

    def show_cost(self):
        return self.cost

    def change_cost(self, new_cost):
        self.cost = new_cost


my_car = Car()
print(my_car.car_name())
my_car.change_car_name('Audi')
print(my_car.name)
print(my_car.car_year_of_production())
my_car.change_car_year_of_production('2019')
print(my_car.year_of_production)
print(my_car.show_manufacturer())
print(my_car.show_capacity())
my_car.change_capacity('3')
print(my_car.engine_capacity)
print(my_car.show_color())
my_car.change_color('red')
print(my_car.color)
print(my_car.show_cost())
my_car.change_cost('30000')
print(my_car.cost)
