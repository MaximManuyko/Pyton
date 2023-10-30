# Условие: Посчитать, сколькими способами можно разменять купюру в 1000 рублей по 500, 200, 100 и 50 рублей.
# Выведите: 
# 1) число вариантов целым числом; 
# 2) все комбинации размена с учетом лимита выдачи банкомата 10 купюр за один раз 


def count_ways_to_exchange(amount):
    # Создаем таблицу для хранения количества способов размена для каждой суммы от 0 до amount.
    # Инициализируем таблицу нулями.
    dp = [0] * (amount + 1)
    
    # У нас всегда есть один способ размена 0 рублей - не разменивать ничего.
    dp[0] = 1

    # Номиналы купюр
    denominations = [500, 200, 100, 50]

    # Для каждого номинала купюры
    for denom in denominations:
        # Начинаем суммировать способы размена, начиная с текущего номинала до amount
        for i in range(denom, amount + 1):
            dp[i] += dp[i - denom]

    # Количество способов размена для заданной суммы находится в последней ячейке таблицы.
    number_of_ways = dp[amount]
    print()
    print("Общее число вариантов размена:", number_of_ways)
    print()
    print("Варианты размена с ограничением 10 купюр:")

    # Добавляем код для вывода всех комбинаций размена
    combinations = []

    def find_combinations(remaining, current_combination, denom_index):
        # Если размен успешно выполнен и количество купюр не превышает 10, сохраняем комбинацию.
        if remaining == 0 and sum(current_combination) <= 10:
            combinations.append(current_combination)
            return
        if denom_index == len(denominations):
            return
        for count in range(11):
            new_combination = current_combination[:]
            new_combination[denom_index] = count
            # Рекурсивно ищем комбинации размена для оставшейся суммы.
            find_combinations(remaining - count * denominations[denom_index], new_combination, denom_index + 1)

    # Начинаем поиск комбинаций размена для заданной суммы и начальной комбинации [0, 0, 0, 0].
    find_combinations(amount, [0, 0, 0, 0], 0)

    # Выводим найденные комбинации размена.
    for i, combination in enumerate(combinations):
        print(f"Вариант {i + 1}; 500 руб. {combination[0]}; 200 руб. {combination[1]}; 100 руб. {combination[2]}; 50 руб. {combination[3]}")

# Вызываем функцию с заданной суммой 1000 рублей
count_ways_to_exchange(1000)
