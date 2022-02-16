# #ДЗ

# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,

st_1 = 'as 23 fdfdg544'
print(st_1)
numbers = []

for item in st_1:
    if item.isdigit():
        numbers.append(int(item))

print(numbers)
print('--------------------------------------------------------')
##################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх так як вони написані

st_2 = 'as 23 fdfdg544 34'
print(st_2)

numbers_2 = []
n = ''
for item in st_2:
    if item.isdigit():
        n += item
    else:
        if n != '':
            numbers_2.append(int(n))
            n = ''
if n != '':
    numbers_2.append(int(n))

print(numbers_2)
print('--------------------------------------------------------')
# #################################################################################
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'
letters = []
for item in greeting:
    letters.append(item.upper())

print(letters)
print('--------------------------------------------------------')
# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
#
list_of_numbers = []

i = 0
while i <= 50:
    if i % 2 == 1:
        list_of_numbers.append(i ** 2)
    i += 1

print(list_of_numbers)
print('--------------------------------------------------------')


# function
#
# - створити функцію яка виводить ліст
def print_list():
    print([1, 2, 3, 4, 5, 6, 7])


print_list()
print('--------------------------------------------------------')


# - створити функцію яка приймає три числа та виводить та повертає найменьше.

def three_numbers(a1, b1, c1):
    min_number = min(a1, b1, c1)
    print(min_number)
    return min_number


print(three_numbers(1, 4, 8))
print('--------------------------------------------------------')


# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def maximun(aa, bb, cc):
    max_number = max(aa, bb, cc)
    print(max_number)
    return max_number


print(maximun(1, 4, 8))
print('--------------------------------------------------------')


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

def some_numbers(*args):
    print(max(*args))
    return min(*args)


print(some_numbers(1, 56, 4, 8, 89, 0))
print('--------------------------------------------------------')


# - створити функцію яка повертає найбільше число з ліста

def some_name(arr):
    max_item = arr[0]
    for element in arr:
        if element > max_item:
            max_item = element
    return max_item


print(some_name([2, 4, 7, 45, 6, 90]))

print('--------------------------------------------------------')


# - створити функцію яка повертає найменьше число з ліста

def some_element(arr):
    min_item = arr[0]
    for ell in arr:
        if ell < min_item:
            min_item = ell
    return min_item


print(some_element([2, 4, 7, 45, 6, 90]))
print('--------------------------------------------------------')


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def sum_element(arr):
    result = 0
    for number in arr:
        result += number
    return result


print(sum_element([1, 2, 3, 4, 5, 6]))

print('--------------------------------------------------------')


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def middle(arr):
    middle_number = 0
    for one in arr:
        middle_number += one
    return middle_number / len(arr)


print(middle([1, 2, 6, 7, 8]))

print('--------------------------------------------------------')

#

# #################################################################################################
# 1)Дан лист:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - найти min число в листе
#   - удалить все дубликаты в листе
#   - заменить каждое четвертое значение на "Х"

list_num = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
print(min(list_num))

print(set(list_num))


def absd(arr):
    for var in range(3, len(arr) - 1, 4):
        arr[var] = 'X'
    return arr


print(absd(list_num))

print('--------------------------------------------------------')


# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:

def print_square(count):
    print("* " * count)
    for start in range(count - 2):
        print("* ", "  " * (count - 3), "* ")
    print("* " * count)


print_square(5)

print('--------------------------------------------------------')
# 3) вывести табличку умножения с помощью цикла while

a = 1
while a < 10:
    b = 1
    while b < 10:
        c = a * b
        print(c, end=" ")
        b += 1
    print(" ")
    a += 1

print('--------------------------------------------------------')
# ***  - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# [-1, -2, 3, 4, 555] => 4
# [5, 5, 5, 5] => 5
# [-10, 5, 5] => 5
array_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def find(arr):
    avg = sum(arr) / int(len(arr))
    copy = arr[:]
    for z, k in enumerate(arr):
        copy[z] = abs(k - avg)
    f = min(copy)
    print(arr[copy.index(f)])


find(array_list)
print('--------------------------------------------------------')
# 4) переделать первое задание под меню с помощью цикла

print('1 - найти min число в листе')
print('2 - удалить все дубликаты в листе')
print('3 - заменить каждое четвертое значение на "Х"')
print(
    '4 - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа')
print('6 - выход')
list_tasks = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
print(list_tasks)
task = int(input(' Сделайте свой выбор: '))

while i != 6:
    if task == 1:
        print(min(list_tasks))
        task = int(input(' Сделайте свой выбор: '))
    elif task == 2:
        print(set(list_tasks))
        task = int(input(' Сделайте свой выбор: '))
    elif task == 3:
        print(absd(list_tasks))
        task = int(input(' Сделайте свой выбор: '))
    elif task == 4:
        find(list_tasks)
        task = int(input(' Сделайте свой выбор: '))
    elif task == 6 or task > 6:
        break

