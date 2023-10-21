# Реализуйте функцию length_of_last_word(), которая возвращает длину последнего слова переданной на вход строки. Словом считается любая последовательность не содержащая пробелы, символы перевода строки \n и табуляции \t.

# length_of_last_word('') # 0
# length_of_last_word('man in Black') # 5
# length_of_last_word('hello, world!     ') # 6
# length_of_last_word('hello\t\nworld') # 5

def length_of_last_word(s):
    # Разбиваем строку по пробелам, символам перевода строки и табуляции,
    # и удаляем пустые строки, чтобы получить список слов.
    words = [word for word in s.split() if word]

    if words:
        # Если список слов не пуст, возвращаем длину последнего слова.
        return len(words[-1])
    else:
        # Если список слов пуст, возвращаем 0.
        return 0

# Примеры использования:
print(length_of_last_word(''))  # 0
print(length_of_last_word('man in Black'))  # 5
print(length_of_last_word('hello, world!     '))  # 6
print(length_of_last_word('hello\t\nworld'))  # 5
