# 1. Написать программу, которая выводит на экран список четных чисел от 10 до 30.

even = []
for number in range(10, 31, 2):
    even.append(number)
print(even)

#
# 2. Написать программу, которая принимает от пользователя ввод трех имен и добавляет их в список names

names = []
for i in range(3):
       name = input("Введите имя: ")
       names.append(name)

# Выведите список на экран
print(names)

# Выведите количество элементов списка
print(len(names))

# Выведите отдельно первый элемент списка
print(names[0])

# Выведите отдельно последний элемент списка
print(names[-1])

# 3. в получившийся во 2 задании список names добавьте имя Igor во 2 позицию
names.insert(1, "Igor")
print(names)

# выведите на экран индекс этого элемента
ind = names.index("Igor")
print(ind)

# удалите имя Igor из списка
names.remove("Igor")
print(names)