# Чтение файла
# Можно открыть только существующий файл !!!
from lesson_3_set import names

# открытие файла в режиме чтения
myfile = open("myfile.txt", "r", encoding="utf-8")
text = myfile.read()
# закрытие файла после всех операций с ним
myfile.close()

# print(text)
# print(len(text))
# print(text.splitlines())
# print(len(text.splitlines()))

# открытие файла в режиме записи (перезаписи)
# new_file = open("new_file.txt", "w", encoding=  "utf-8")
# text = "I love Python!"
# new_file.write(text+'\n')
# new_file.write("Python forever!!!")
#
# names = ["Masha", "Sasha", "Ivan"]
# for word in names:
#     new_file.write(word+'\n')
#
# names_string = "\n".join(names)
# new_file.write(names_string+'\n')
# new_file.close()

new_file = open("new_file.txt", "a", encoding=  "utf-8")
new_file.write("\nNEW TEXT")
new_file.close()