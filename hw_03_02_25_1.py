# 1. создайте текстовый файл task_1.txt при помощи python.
task_1 = open("task_1.txt", "w", encoding= "utf-8")

# 2. запишите в него следующий текст: Пословицы – неотъемлемая часть повседневной речи каждого Русского человека.
text = "Пословицы - неотъемлемая часть повседневной речи каждого Русского человека."
task_1.write(text)
task_1.close()

# 3. считайте файл в программу
task_1 = open("task_1.txt","r",encoding= "utf-8")
print(task_1.read())
task_1.close()

# 4. Выведите на экран следуюущую информацию с пояснениями:

# - первый символ текста
print(f"{text[0]} - первый символ текста.")

# - последний символ текста
print(f"{text[-1]} - последний символ текста.")

# - первые три символа
print(f"{text[0:3]} - первые три символа.")

# - последние три символа
print(f"{text[-3:]} - последние три символа.")

# - первое слово
new_list = text.strip('-.').replace('-', '').split()
print(f"{new_list[0]} - первое слово.")

# - последнее слово
print(f"{new_list[-1]} - последнее слово.")

# - количество символов
print(f"{len(text)} - количество символов текста.")

# - количество слов
print(f"{len(new_list)} - количество слов текста.")

# - тест в верхнем регистре
print(f"{text.upper()} - текст в верхнем регистре")

# - текст в нижнем регистре
print(f"{text.lower()} - текст в нижнем регистре")