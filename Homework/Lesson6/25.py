# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования ** лямбд, filter, map, zip, enumerate, list comprehension


my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из этого абв текста все вабвс слова, содерабващие содержащие "абв"'


def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)


my_text = del_some_words(my_text)
print(my_text)
