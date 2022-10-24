def view():
    point = -1

    text_menu = ("МЕНЮ - Телефонный справочник\n"
                 "1. Вывести базу\n"
                 "2. Добавить ключ\n"
                 "3. Добавить пользователя\n"
                 )
    print(text_menu)

    while True:
        try:
            point = int(input("Введите номер пункта меню: "))
            if point in [1, 2, 3]:
                break
        except ValueError:
            print("Введён неправильный пункт меню. Попробуйте ещё раз.")
    return point
