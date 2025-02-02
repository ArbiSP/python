# 1. Пользователь с клавиатуры вводит текст. Запишите этот текст в файл text1.txt.
in_text = input("Введите текст: ")
text1 = open("text1.txt", "w", encoding= "utf-8")
text1.write(in_text+'\n')
text1.close()

# 2. Пользователь с клавиатуры вводит текст. Добавьте этот текст в конец файла text1.txt
in_text = input("Введите текст: ")
text1 = open("text1.txt", "a", encoding= "utf-8")
text1.write(in_text+'\n')
text1.close()

# 3. Выведите на экран содержимое файла text1.txt

text1 = open("text1.txt","r",encoding= "utf-8")
print(text1.read())
text1.close()
