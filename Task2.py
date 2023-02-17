# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

class Book:
    name = 'Різдвяна свинка'
    year = '2021'
    publisher = 'А-БА-БА-ГА-ЛА-МА-ГА'
    genre = 'childrens novel'
    author = 'J.K. Rowling'
    price = '400 uah'

    def book_name(self):
        return self.name

    def change_book_name(self, new_book_name):
        self.name = new_book_name

    def book_year(self):
        return self.year

    def change_book_year(self, new_year):
        self.year = new_year

    def show_publisher(self):
        return self.publisher

    def change_publisher(self, new_publisher):
        self.publisher = new_publisher

    def show_genre(self):
        return self.genre

    def change_genre(self, new_genre):
        self.genre = new_genre

    def show_author(self):
        return self.author

    def change_author(self, new_author):
        self.author = new_author

    def show_price(self):
        return self.price

    def change_price(self, new_price):
        self.price = new_price


my_book = Book()
print(my_book.book_name())
my_book.change_book_name('It ends with us')
print(my_book.name)
print(my_book.book_year())
my_book.change_book_year('2016')
print(my_book.year)
print(my_book.show_publisher())
my_book.change_publisher('Atria Books')
print(my_book.publisher)
print(my_book.show_genre())
my_book.change_genre('Romance')
print(my_book.genre)
print(my_book.show_author())
my_book.change_author('Colleen Hoover')
print(my_book.author)
print(my_book.show_price())
my_book.change_price('290 uah')
print(my_book.price)
