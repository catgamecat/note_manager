username = input("Как вас зовут? ")
content = input("Пишите: ")
status = input("Статус заметки (Активно/Завершено/Просрочено): ")
created_date = input("Дата создания заметки (ДД-ММ-ГГГГ): ")
change_date = input("Дата изменения заметки (ДД-ММ-ГГГГ): ")
title_1 = input("Введите название заголовка: ")
title_2 = input("Введите название заголовка: ")
title_3 = input("Введите название заголовка: ")
note = [username, content, status, created_date, change_date, [title_1, title_2, title_3]]
print(f"Имя пользователя: {note[0]}",
    f"\nСодержание заметки: {note[1]}",
    f"\nСтатус: {note[2]}",
    f"\nДата создания: {note[3]}",
    f"\nДата изменения: {note[4]}",
    f"\nЗаголовки: {note[5]}")