# #Списки
# names = []
#  # добавление элемента в конец списка
# names.append(2)
# names.append("Alex")
# my_name = "Elena"
# names.append(my_name)
#
# # получить элемент списка (с удалением его из списка)
#
# last_name = names.pop()
# print(last_name)
# print(names)
#
# # подсчет кол-ва элемента в списке
# print(names.count("24e343"))
#
# names.append("Alex")
# print(names)
# ind = names.index("Alex", 1,3)
# print(ind)
#
# # добавление элемента в произвольное место списка
# names.insert(0, "Masha")
# print(names)
#
# names.remove("Alex")
# print(names)
#
# # кол-во элементов в списке
# print(names[0])
# print(names[-2])
#
# # срезы списка
#
# names.extend(["Dima", "Vova", "Sergey"])
# print(names[5:1:-1])
# print(names[::-1])
#
# # цикл  For
# # проход по элементам коллекции
# for i in names:
#     print(i)
# # range(6) = (0,1,2,3,4,5)
# # range(1,5) = (1,2,3,4)
# for i in range(len(names)):
#     print(f"{i+1}.{names[i]}")
#
# a = 10
# while a > 0:
#     print("Hello")
#     a -= 4
#     if a == 4:
#          break
# # print("Выберите действие: ")
# # print("1. Добавить книгу")
# # print("2. Удалить книгу")
# # print("Введите 0 для выхода из меню ")
# #
# # action = input(">>> ")
# # if  action == "1":
# #     print("Книга добавлена")
# # elif action == "2":
# #     print("Книга удалена")
# # elif action == "0":
# #     print("До свидания")
#
# a = 1
# while a < 9:
#     print(a)
#     a += 9
#
# # кортеж
# # tuple
# numbers = (1,2,3,4)
# status = (
#     ("in_progress", "В работе"),
#     ("success", "Выполнено"),
# )
#
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
# ключом словаря может быть ьолько неизменяемый тип данных (строка, число, кортеж)
cars = {("bmw", "audi"): "germany"}
#
# age = info.pop("age")
# print(age)
# print(info)
#
# print(info)
# info_copy = info
# print((info_copy))
# print(id(info))
# print(id(info_copy))
# info["XXX"] = "YYY"
# print(info_copy)
#
# new_info = info.copy()
# print(id(info))
# print(id(new_info))
#
# users = []
# info_person = {}
# for i in range(3):
#      name = input("Enter the name: ")
#      phone = input("Enter the phone: ")
#      info_person["name"] = name
#      info_person["phone"] = phone
#      users.append(info_person)

#print(users)

print(list(info.keys()))
print(list(info.items()))

for i in info:
    print(f"{i} - {info[i]}")

for key, value in info.items():
    print(f"{key} ---- {value}")