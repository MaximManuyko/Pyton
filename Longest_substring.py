# Реализуйте функцию find_longest_length(), принимающую на вход строку и возвращающую длину максимальной последовательности из неповторяющихся символов. Подстрока может состоять из одного символа. Например, в строке qweqrty, можно выделить следующие подстроки: qwe, weqrty. Самой длинной будет weqrty, а её длина — 6 символов.

# find_longest_length('abcdeef')  # 5
# find_longest_length('jabjcdel')  # 7

def find_longest_length(s):
    # Создаем словарь для отслеживания индексов символов
    char_index = {}
    max_length = 0
    start = 0  # Начало текущей подстроки

    for end in range(len(s)):
        # Если символ уже встречался и его индекс больше или равен началу текущей подстроки
        if s[end] in char_index and char_index[s[end]] >= start:
            # Обновляем начало текущей подстроки
            start = char_index[s[end]] + 1

        # Обновляем индекс символа
        char_index[s[end]] = end

        # Вычисляем текущую длину подстроки
        current_length = end - start + 1

        # Обновляем максимальную длину, если необходимо
        max_length = max(max_length, current_length)

    return max_length

# Примеры использования:
print(find_longest_length('abcdeef'))  # 5
print(find_longest_length('jabjcdel'))  # 7
