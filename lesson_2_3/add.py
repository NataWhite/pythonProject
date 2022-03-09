# вивести послідовність Фібоначі, кількість вказана в знінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел)

# def fibonachi(count):
#     i = 0
#     arr = [1]
#     n = arr[i]
#     while i <= count - 2:
#         arr.append(n)
#         n = n + arr[i]
#         i += 1
#     return arr
#
#
# print(fibonachi(10))

################################

# n = int(input('enter count of numbers: '))
#
#
# def fibonachi(count):
#     fib_number_1 = fib_number_2 = 1
#     print(fib_number_1, fib_number_2, end=' ')
#
#     for i in range(2, count):
#         fib_number_1, fib_number_2 = fib_number_2, fib_number_1 + fib_number_2
#         print(fib_number_2, end=' ')
#
#
# fibonachi(n)

###################################################

# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3

# def counter_of_numbers(number):
#     count_p = 0
#     count_n = 0
#     for item in number:
#         if int(item) % 2 == 0:
#             count_p += 1
#         else:
#             count_n += 1
#     print('непарних чисел:', count_n, 'парних чисел:', count_p)
#
#
# num = input('Enter a number: ')
# counter_of_numbers(num)

########################################################

# Знайти анаграму.
# //     Перевірити чи слово має в собі такі самі літери як і поеперднє слово.
# //
# //     ANAGRAM | MGANRAA -> true
# // EXIT | AXET -> false
# // GOOD | DOGO -> true

# def anagram(word1, word2):
#     list1 = []
#     list2 = []
#
#     list1[:0] = word1
#     list1.sort()
#     first = ''.join(list1)
#
#     list2[:0] = word2
#     list2.sort()
#     second = ''.join(list2)
#
#     return first == second
#
#
# print(anagram('ANAGRAM', 'MGANRAA'))
# print(anagram('EXIT', 'AXET'))

#############################################
# Сумма цифр числа
# // Дано натуральное число N. Вычислите сумму его цифр.
# //     При решении этой задачи нельзя использовать строки,
# //     списки, массивы ну и циклы, разумеется.
# //     Рекурсія)
# from functools import reduce
#
# numbers = []
#
#
# def sum_num(n):
#     numbers.append(n % 10)
#     if n < 10:
#         return
#     else:
#         next_n = round(n / 10)
#         sum_num(next_n)
#     return reduce(lambda x, y: x + y, numbers)
#
#
# print(sum_num(1223))

###############################################################
# Знайти набільший елемент в масиві за допомогою reduce
# //     [1,6,9,0,17,88,4,7] -> 88

# from functools import reduce
#
# items = [1, 24, 17, 14, 119, 32, 2]
# max_numb = reduce(lambda a, b: a if (a > b) else b, items)
#
# print(max_numb)

################################################################
# Количество единиц
# // Дана последовательность натуральных чисел  в строке, завершающаяся двумя числами 0 подряд.
# // Определите, сколько раз в этой последовательности встречается число 1. Числа, идущие после двух нулей, необходимо игнорировать.
# //
# // 2176491947586100 -> 3

# def count_of_one(string):
#     count = 0
#     for i in range(len(string)):
#         if string[i] == '1':
#             count += 1
#         if string[i] == string[i + 1]:
#             return count
#
#
# print(count_of_one('2176491947586100'))
