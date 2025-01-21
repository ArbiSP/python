#Списки
names = []
# добавление элемента в конец списка
names.append(2)
names.append("Alex")
my_name = "Elena"
names.append(my_name)

# получить элемент списка (с удалением его из списка)

last_name = names.pop(0)
print(last_name)
print(names)

# подсчет кол-ва элемента в списке
print(names.count("24e343"))

# поиск первого индекса элемента
names.append("Alex")
# print(names)
# ind = names.index("Alex", 1,3)
# print(ind)

# добавление элемента в произвольное место списка
names.insert(0, "Masha")
# print(names)

# удаление элемента из списка по его значению
names.remove("Alex")
# print(names)

# количество элементов в списке
#print(len(names))

# получение элементов списка
# print(names[0])
# print(names[1])

# срезы списка
names.extend(["Dima", "Vova", "Sergey"])
# print(names[5:1:-1])
# print(names[::-1])


# цикл  For
# проход по элементам коллекции
# for i in names:
#     print(i)

# range(6) = (0,1,2,3,4,5)
# range(1,5) = (1,2,3,4)

# for i in range(len(names)):
#      print(f"{i+1}.{names[i]}")
#
# a = 10
#
# while a > 0:
#      print("Hello")
#      a -= 4
#      if a == 4:
#           break

# while True:
#     print("Выберите действие: ")
#     print("1. Добавить книгу")
#     print("2. Удалить книгу")
#     print("Введите 0 для выхода из меню ")
#
#     action = input(">>> ")
#     if  action == "1":
#         print("Книга добавлена")
#     elif action == "2":
#         print("Книга удалена")
#     elif action == "0":
#         print("До свидания")
#         break
#     else:
#         print("Выберите нужный пункт меню!!!")

print(names)
names += ["Nastya", "Olga"]
print(names)

# for i in range(1, 10):
#     print(i)

# кортеж
# tuple

numbers = (1,2,3,4)
status = (
    ("in_progress", "В работе"),
    ("success", "Выполнено"),
 )

print("Hello")
print(len("Dima"))


# словарь
person = {}
info = {"name": "Dima", "age": 26}

# получение элемента словаря
name = info["name"]
print(info["name"])

# добавление элемента в словарь
info["phone"] = "8961545784"

# обновление значения элемента
info["name"] = "Sergey"

# размер словаря = кол-во элементов (пар, ключей)
print(len(info))
info["lang"] = ["russian", "english"]
print(info)
info["edu"] = {"hight": "MGU", "medium": "ITMO"}
print(info)

# ключом словаря может быть только неизменяемый тип данных (строка, число, кортеж)
cars = {("bmw", "audi"): "germany"}

age = info.pop("age")
print(age)
print(info)

# print(info["age"])
print(info.get("edu", {}). get("hight", {}))

print(info)

info_copy = info
print((info_copy))
print(id(info))
print(id(info_copy))
info["XXX"] = "YYY"
print(info_copy)

new_info = info.copy()
print(id(info))
print(id(new_info))


users = []


# for i in range(3):
#       name = input("Enter the name: ")
#       phone = input("Enter the phone: ")
#       info_person = {"name": name, "phone": phone}
#
#       users.append(info_person)
#
# print(users)

# print(list(info.keys()))
# print(list(info.values()))
# print(list(info.items()))
# info.update({"name": "sdsd", "age": 234})

# for key in info:
#     print(f"{key} - {info[key]}")

for key, value in info.items():
    print(f"{key} ---- {value}")