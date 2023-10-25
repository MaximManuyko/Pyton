# Реализуйте функцию-предикат scrabble, которая принимает на вход два параметра: набор символов (строку) и слово. Функция должна проверять, можно ли из переданного набора составить это слово. В результате вызова функция возвращает True или False.

# При проверке учитывается количество символов, которые нужны для составления слова, но не учитывается их регистр.

# Для решения используйте встроенный инструмент — Counter.

# Пример
# scrabble('rkqodlw', 'world')  # True
# scrabble('avj', 'java')  # False
# scrabble('avjafff', 'java')  # True
# scrabble('', 'hexlet')  # False
# scrabble('scriptingjava', 'JavaScript')  # True

from collections import Counter

def scrabble(available_letters, word):
    # Преобразуем оба входных параметра в нижний регистр для учета регистронезависимости
    available_letters = available_letters.lower()
    word = word.lower()

    # Подсчитываем количество каждого символа в доступных буквах и в слове
    available_letters_count = Counter(available_letters)
    word_count = Counter(word)

    # Проверяем, что для каждой буквы в слове есть достаточно букв в доступных буквах
    for letter, count in word_count.items():
        if available_letters_count[letter] < count:
            return False

    # Если цикл завершился, это означает, что все буквы в слове могут быть составлены из доступных букв
    return True

# Тестируем функцию
print(scrabble('rkqodlw', 'world'))  # True
print(scrabble('avj', 'java'))  # False
print(scrabble('avjafff', 'java'))  # True
print(scrabble('', 'hexlet'))  # False
print(scrabble('scriptingjava', 'JavaScript'))  # True
