# Иногда в программировании возникает задача поиска разницы между двумя наборами данных — например, между словарями или json-файлами. Для этого даже существуют специальные сервисы, например, http://www.jsondiff.com/. Попробуйте нажать на ссылку sample data и затем кнопку Compare.

# src/solution.py

# Реализуйте функцию gen_diff, которая сравнивает два словаря и возвращает результат сравнения в виде словаря. Ключами результирующего словаря будут все ключи из двух входящих, а значением строка с описанием отличий: added, deleted, changed или unchanged.

# Возможные значения:

# added — ключ отсутствовал в первом словаре, но был добавлен во второй
# deleted — ключ был в первом словаре, но отсутствует во втором
# changed — ключ присутствовал и в первом и во втором словаре, но значения отличаются
# unchanged — ключ присутствовал и в первом и во втором словаре с одинаковыми значениями
# Пример работы:

# from solution import gen_diff

# gen_diff(
#     {"one": "eon", "two": "two", "four": True},
#     {"two": "own", "zero": 4, "four": True},
# )
# # {"one": "deleted", "two": "changed", "four": "unchanged", "zero": "added"}

def gen_diff(dict1, dict2):
    result = {}
    
    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())
    
    # Обработка ключей, которые присутствуют только в первом словаре
    for key in keys1 - keys2:
        result[key] = "deleted"
    
    # Обработка ключей, которые присутствуют только во втором словаре
    for key in keys2 - keys1:
        result[key] = "added"
    
    # Обработка ключей, которые присутствуют в обоих словарях
    for key in keys1 & keys2:
        if dict1[key] == dict2[key]:
            result[key] = "unchanged"
        else:
            result[key] = "changed"
    
    return result

# Пример использования:
dict1 = {"one": "eon", "two": "two", "four": True}
dict2 = {"two": "own", "zero": 4, "four": True}
result = gen_diff(dict1, dict2)
print(result)  # {"one": "deleted", "two": "changed", "four": "unchanged", "zero": "added"}
