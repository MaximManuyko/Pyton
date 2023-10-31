# Query String (строка запроса) — это часть URL, содержащая константы и их значения. Она начинается после вопросительного знака и идет до конца адреса:

# # query string: page=5
# https://ru.hexlet.io/blog?page=5
# Если параметров несколько, то они отделяются амперсандом &:

# # query string: page=5&per=10
# https://ru.hexlet.io/blog?per=10&page=5
# src/solution.py
# Напишите функцию build_query_string, которая принимает на вход словарь с параметрами и возвращает строку запроса, сформированную из этих параметров:

# build_query_string({'per': 10, 'page': 1}) # 'page=1&per=10'
# Подсказки
# Тесты ожидают, что параметры будут отсортированы, поэтому воспользуйтесь функцией sorted().

# Чтобы собрать строку из нескольких кусков с помощью некоторого разделителя, вы можете воспользоваться таким способом:

# ','.join(['abc', 'cde', 'def']) # 'abc,cde,def'

def build_query_string(params):
    # Сортируем параметры по ключам
    sorted_params = sorted(params.items())
    
    # Создаем список из строк вида 'ключ=значение'
    param_strings = [f"{key}={value}" for key, value in sorted_params]
    
    # Объединяем строки с помощью символа '&'
    query_string = '&'.join(param_strings)
    
    return query_string

# Пример использования:
params = {'per': 10, 'page': 1}
query_string = build_query_string(params)
print(query_string)  # 'page=1&per=10'
