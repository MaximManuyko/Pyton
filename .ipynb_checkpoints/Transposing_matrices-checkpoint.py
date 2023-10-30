# Реализуйте функцию transposed(), которая должна принимать матрицу в виде списка списков и возвращать транспонированную матрицу (новый список списков).

# Имейте в виду, что хоть в математике и транспонируют строго квадратные матрицы, ваша функция transposed() должна быть более "всеядной": она должна уметь переворачивать и прямоугольные матрицы!

# transposed([[1]])  # [[1]]
# transposed([[1, 2], [3, 4]])  # [[1, 3], [2, 4]]
# transposed([[1, 2], [3, 4], [5, 6]])  # [[1, 3, 5], [2, 4, 6]]
# transposed(transposed([[1, 2]])) == [[1, 2]]  # True

def transposed(matrix):
    # Проверяем, пуста ли матрица
    if not matrix:
        return []

    # Получим количество строк и столбцов в исходной матрице
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Создаем новую матрицу, начально заполненную нулями
    transposed_matrix = [[0] * num_rows for _ in range(num_cols)]

    # Заполняем новую матрицу значениями из исходной матрицы
    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

# Примеры использования
print(transposed([[1]]))  # [[1]]
print(transposed([[1, 2], [3, 4]]))  # [[1, 3], [2, 4]]
print(transposed([[1, 2], [3, 4], [5, 6]]))  # [[1, 3, 5], [2, 4, 6]]
print(transposed(transposed([[1, 2]])) == [[1, 2]])  # True
