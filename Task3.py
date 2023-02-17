# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

class Stadium:
    name = 'Chornomorets Stadium'
    opening_date = '18.05.1936'
    country = 'Ukraine'
    city = 'Odesa'
    capacity = '34164'

    def show_name(self):
        return self.name

    def change_name(self, new_name):
        self.name = new_name

    def show_opening_date(self):
        return self.opening_date

    def change_opening_date(self, new_opening_date):
        self.opening_date = new_opening_date

    def show_country(self):
        return self.country

    def change_country(self, new_country):
        self.country = new_country

    def show_city(self):
        return self.city

    def change_city(self, new_city):
        self.city = new_city

    def show_capacity(self):
        return self.capacity

    def change_capacity(self, new_capacity):
        self.capacity = new_capacity


stadium = Stadium()
print(stadium.show_name())
stadium.change_name('НСК Олімпійський')
print(stadium.name)
print(stadium.show_opening_date())
stadium.change_opening_date('12.05.1996')
print(stadium.opening_date)
print(stadium.show_country())
print(stadium.show_city())
stadium.change_city('Kyiv')
print(stadium.city)
print(stadium.show_capacity())
stadium.change_capacity('70050')
print(stadium.capacity)