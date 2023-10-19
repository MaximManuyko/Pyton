# Реализуйте функцию sum_of_intervals(), которая принимает на вход список интервалов и возвращает сумму всех длин интервалов. В данной задаче используются только интервалы целых положительных чисел, которые представлены в виде списков. Первое значение интервала всегда будет меньше, чем второе значение. Например, длина интервала [1, 5] равна 4, а длина интервала [5, 5] равна 0. Пересекающиеся интервалы должны учитываться только один раз.

# from solution import sum_of_intervals
# sum_of_intervals([
#     [1, 1],
# ])
# # 0
# sum_of_intervals([
#     [1, 2],
#     [50, 100],
#     [60, 70],
# ])
# # 51
# sum_of_intervals([
#     [1, 2],
#     [5, 10],
# ])
# # 6***


def sum_of_intervals(intervals):
    # Создаем пустой список, в который будем добавлять уникальные числа из интервалов
    unique_numbers = []
    
    # Перебираем интервалы и добавляем их числа в список unique_numbers
    for interval in intervals:
        for num in range(interval[0], interval[1]):
            if num not in unique_numbers:
                unique_numbers.append(num)
    
    # Считаем сумму длин интервалов
    total_length = len(unique_numbers)
    
    return total_length

# Примеры использования
print(sum_of_intervals([[1, 1]]))  # 0
print(sum_of_intervals([[1, 2], [50, 100], [60, 70]]))  # 51
print(sum_of_intervals([[1, 2], [5, 10]]))  # 6
