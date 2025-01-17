# Матрицу можно представить в виде двумерного списка. Например, список [[1, 2, 3, 4], [5, 6, 7, 8]] — это отображение матрицы:

# 1 2 3 4
# 5 6 7 8
# Реализуйте функцию snail_path(), которая принимает на вход матрицу и возвращает список элементов матрицы по порядку следования от левого верхнего элемента по часовой стрелке к внутреннему. Движение по матрице напоминает улитку:

# Путь улитки Snail path

# from solution import snail_path
# snail_path([[1, 2], [3, 4]])
# # [1, 2, 4, 3]
# snail_path([[1, 2, 3], [8, 9, 4], [7, 6, 5]])
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# snail_path([['b', 'c', 'a'], ['3', True, 11], [None, 'foo', 0]])
# # ['b', 'c', 'a', 11, 0, 'foo', None, '3', True]

def snail_path(matrix):
    result = []
    while matrix:
        result += matrix[0]  # Добавляем верхнюю строку
        matrix = list(zip(*matrix[1:]))  # Вращаем матрицу против часовой стрелки
        matrix.reverse()  # Разворачиваем матрицу
    return result
