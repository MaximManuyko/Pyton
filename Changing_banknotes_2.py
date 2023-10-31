# Функция для подсчета числа вариантов размена
def number_of_exchange_options():
    denominations = [500, 200, 100, 50]
    amount = 1000

    dp = [0] * (amount + 1)
    dp[0] = 1

    for denom in denominations:
        for i in range(denom, amount + 1):
            dp[i] += dp[i - denom]

    return dp[amount]

print("Число вариантов размена:", number_of_exchange_options())

# Функция для вывода всех комбинаций размена с учетом ограничения на общее количество банкнот
def banknotes_10(limit):
    combinations = []

    for num_500s in range(limit + 1):
        for num_200s in range(limit + 1):
            for num_100s in range(limit + 1):
                for num_50s in range(limit + 1):
                    if (num_500s * 500 + num_200s * 200 + num_100s * 100 + num_50s * 50) == 1000 and (num_500s + num_200s + num_100s + num_50s) <= limit:
                        combinations.append((num_500s, num_200s, num_100s, num_50s))

    return combinations

limit = 10
combinations = banknotes_10(limit)
for combination in combinations:
    print(combination)


