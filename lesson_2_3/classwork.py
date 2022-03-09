###############################################################################
# ClassWork_1
###############################################################################
# створити пустый список users_list = []
# стврорити меню в якому потрібно реалізувати:
# 1) додававання нового юзера
# 2) вивід всіх юзерів
# 3) вивід всіх юзерів за віком
# 4) видалення юзера по id
# 5) заміна статуса юзера на протилежний
# 6) вихід з меню
# приклад юзера {'id':1,'name':'Max', 'age':35,'status':False}
###############################################################################

# import time
#
# timestamp = int(time.time())
#
# users_list = []
#
# print('1) додававання нового юзера\n2) вивід всіх юзерів\n3) вивід всіх юзерів за віком\n4) видалення юзера по id\n' +
#       '5) заміна статуса юзера на протилежний\n6) вихід з меню')
#
# task = input('Зроби свій вибір: ')
#
# while True:
#     if task == '1':
#         name = input('Введіть ім"я: ')
#         age = input('Введіть вік: ')
#         status = input('Ввведіть статус: ')
#         users_list.append({'id': timestamp, 'name': name, 'age': int(age), 'status': bool(status)})
#         task = input('Зроби свій вибір: ')
#     elif task == '2':
#         print('All users - ', users_list)
#         task = input('Зроби свій вибір: ')
#     elif task == '3':
#         print('list - ', sorted(users_list, key=lambda user: user['age']))
#         task = input('Зроби свій вибір: ')
#     elif task == '4':
#         user_id = input('user_id: ')
#         for item in users_list:
#             if item['id'] == int(user_id):
#                 users_list.remove(item)
#         task = input('Зроби свій вибір: ')
#     elif task == '5':
#         for user in users_list:
#             user['status'] = not user['status']
#         print(users_list)
#         task = input('Зроби свій вибір: ')
#     elif task == '6':
#         break
#     else:
#         print('введіть число від 1 до 6')

###############################################################################
# ClassWork_2
###############################################################################
# создать декоратор который будет считать сколько раз была запущена функция и будет выводит это значение
# после каждого запуска функции
###############################################################################

# def decorator_count(func):
#     count = 0
#
#     def counter():
#         nonlocal count
#         count += 1
#         func()
#         print(count)
#
#     return counter
#
#
# @decorator_count
# def hello():
#     print('hello')
#
#
# @decorator_count
# def hello2():
#     print('hello2')
#
#
# hello()
# hello()
# hello2()
# hello()

###############################################################################
# кому это очень легко то сделайте функцию на замыкания которая будет возвращать декоратор который
# будет считать общее количество запущенных  функций декорированных этим декоратором
###############################################################################

# def make_decor():
#     count = 0
#
#     def decorator_count(func):
#         def counter():
#             nonlocal count
#             count += 1
#             func()
#             print(count)
#         return counter
#     return decorator_count
#
#
# decorator = make_decor()
#
#
# @decorator
# def hello():
#     print('hello')
#
#
# @decorator
# def hello2():
#     print('hello2')
#
#
# hello()
# hello()
# hello2()
# hello()

###############################################################################
# ClassWork_3
###############################################################################
# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон
###############################################################################
# class Rectangle:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return f'sum: {(self.x * self.y) + (other.x * other.y)}'
#
#     def __sub__(self, other):
#         return f'difference: {(self.x * self.y) - (other.x * other.y)}'
#
#     def __eq__(self, other):
#         return f'equal: {(self.x * self.y) == (other.x * other.y)}'
#
#     def __ne__(self, other):
#         return f'not equal: {(self.x * self.y) != (other.x * other.y)}'
#
#     def __gt__(self, other):
#         return f'gt: {(self.x * self.y) > (other.x * other.y)}'
#
#     def __lt__(self, other):
#         return f'lt: {(self.x * self.y) < (other.x * other.y)}'
#
#     def __len__(self):
#         return (self.x + self.y) * 2
#
#
# rectangle1 = Rectangle(2, 5)
# rectangle2 = Rectangle(4, 10)
#
# print((rectangle1 + rectangle2))
# print((rectangle1 - rectangle2))
# print((rectangle1 == rectangle2))
# print((rectangle1 != rectangle2))
# print((rectangle1 > rectangle2))
# print((rectangle1 < rectangle2))
# print(len(rectangle1))

################################################################################
# создать класс Human (name, age)
# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает
# лист золушек и ищет ту самую

# класса золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количество
################################################################################
# from typing import List
#
#
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Cinderella(Human):
#     count = 0
#
#     def __init__(self, name, age, size):
#         super().__init__(name, age)
#         self.size = size
#         Cinderella.count += 1
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
#     def __str__(self):
#         return f'your love is {self.name}, {self.size}'
#
#
# class Prince(Human):
#     def __init__(self, name, age, shoes):
#         super().__init__(name, age)
#         self.shoes = shoes
#
#     def find_love(self, girls: List[Cinderella]):
#         for item in girls:
#             if item.size == self.shoes:
#                 return item
#
#
# girls = [
#     Cinderella('Olia', 23, 36),
#     Cinderella('Tanya', 24, 37),
#     Cinderella('Cocos', 25, 38)
# ]
#
# prince = Prince('Vasya', 27, 37)
#
# print(Prince.find_love(prince, girls))
