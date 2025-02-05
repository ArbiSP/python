from functools import  reduce


def get_sum_numbers(num_1=0, num_2=0):
    return num_1 + num_2

# def get_first_last_char(text):
#     first = text[0]
#     last = text[-1]
#     second = text[1]
#
#     return  first, last, second
#
# result = (get_first_last_char(text="python"))
#

# def get_max_value(numbers):
#     max_val = numbers[0]
#     for i in numbers:
#         if i > max_val:
#             max_val = i
#     return max_val
#
# def get_min_value(numbers):
#     min_val = numbers[0]
#     for i in numbers:
#         if i < min_val:
#             min_val = i
#     return min_val
#
# def get_sum_even_numbers(numbers):
#     sum_ = 0
#     for i in numbers:
#         if i % 2 == 0:
#             sum_ += i
#     return sum_
#
# def get_clean_words(text):
#     pass

# nums = [1,9,6,8,-1,7]
# max_v = get_max_value(numbers=nums)
# min_v = get_min_value(numbers=nums)
# print(max_v)
# print(min_v)
# sum_numbers = get_sum_even_numbers(numbers=nums)
# print(sum_numbers)
text = "I,Love - Python"
text = (text.replace(',', ' ').replace('-',' '))
new_list = text.lower().split()

# lambda - функции

def square(x):
    return x*x

def sum_num(a, b):
    return a + b

sum_ = lambda x,y: x +y
print(sum_(2, 3))

square_ = lambda x: x*x
print(square_(2))

# message = lambda: print("hello")


# new_list = list(map(lambda x: x.lower(), text))
# [i , love , python]

# функции высшего порядка
# принимают в качестве параметров другую фунцию

# map - применяется для преобразования элементов,
# применяя к каждому элементу заданную функцию

numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda  x: x*x, numbers))
print(squared_numbers)

list_of_words = ["AAA", "BBB", "CCC"]
lower_words = list(map(lambda x: x.lower(), list_of_words))
print(lower_words)

# filter - используется для фильтрации элементов,
# оставляя только те, для которых заданная функция возвращает True

numbers_2 = [1,2,3,4,5,6,7,8,9]
even_numbers = list(filter(lambda x: x % 2 ==0, numbers_2))
print(even_numbers)

# reduce - последовательное применение функции к элементам
# с целью свести их к одному значению

sum_of_numbers = reduce(lambda x,y: x + y, numbers_2)
print(sum_of_numbers)
min_value = reduce(lambda x, y: x if x < y else y, numbers_2)
print(min_value)
x = 5
y = 8

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
a = is_even(5)
b = is_even(6)
print(a, b)