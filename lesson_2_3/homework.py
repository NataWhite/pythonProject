# написать функцию на замыкания которая будет в себе хранить лист дел,
# вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи
#
# запишите 5 тудушек
# и выведете все

# 2) протипизировать первое задание
###############################################################################

from typing import List

# def notebook() -> List:
#     todo_list: List[str] = []
#     number: int = 0
#
#     def add_todo():
#         while len(todo_list) < 5:
#             todo: str = input('записати в блокнот завдання: ')
#             todo_list.append(todo)
#
#     def get_all():
#         nonlocal number
#         for item in todo_list:
#             number += 1
#             print(number, ' -- ', item)
#
#     return [add_todo, get_all]
#
#
# write, show_list = notebook()
# write()
# show_list()


###############################################################################
# 3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)
#
# Пример:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
###############################################################################

# def expanded_form(numb: int) -> str:
#     string = str(numb)
#     array: List[str] = []
#     zero: str = ''
#     for i in reversed(string):
#         if i != '0':
#             array.append(i + zero)
#         zero += '0'
#     return '+'.join(array[::-1])
#
#
# print(expanded_form(70304))

################################################################################
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable

from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        print(self.name)


class Magazine(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        print(self.name)


##################################################################
# 3) Створити свій кастомний Exception
# 4) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають
# є класом Book або Magazine інакше кидати свою кастомну помилку
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
#
# 4)всі методи класу Main запускати в try except, приклад:
# try:
#     Main.add(Magazine('Magazine1'))
#     Main.add(Book('Book1'))
#     Main.add(Magazine('Magazine3'))
#     Main.add(Magazine('Magazine2'))
#     Main.add(Book('Book2'))
#
#     Main.show_all_magazineі()
#     print('-' * 40)
#     Main.show_all_bookі()
# except NonBookMagazineException:
#     print('Це не журнал або книжка')
# except Exception as err:
#     print(err)

class MyCustomException(Exception):
    print('Це не журнал або книжка')


class Main:
    printable_list = []

    @classmethod
    def add(cls, new_element):
        if not isinstance(new_element, (Book, Magazine)):
            raise MyCustomException
        cls.printable_list.append(new_element)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()


try:
    Main.add(Magazine('Magazine1'))
    Main.add(Book('Book1'))
    Main.add(Magazine('Magazine3'))
    Main.add(Magazine('Magazine2'))
    Main.add(Book('Book2'))

    Main.show_all_magazines()
    print('-' * 40)
    Main.show_all_books()
    Main.add(True)
except MyCustomException:
    print('Це не журнал або книжка')
except Exception as err:
    print(err)
