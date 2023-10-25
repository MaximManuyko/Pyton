# Запрос суммы у пользователя
sum_input = float(input("Введите сумму(Руб.): "))

# Номиналы купюр
nominals = [5000, 2000, 1000, 500, 100, 50, 10, 1]

# Переменные для хранения количества купюр каждого номинала
k_5000 = 0
k_2000 = 0
k_1000 = 0
k_500 = 0
k_100 = 0
k_50 = 0
k_10 = 0
k_1 = 0

# Вычисление минимального количества купюр
for nominal in nominals:
    if sum_input >= nominal:
        count = int(sum_input // nominal)
        sum_input -= count * nominal
        if nominal == 5000:
            k_5000 = count
        elif nominal == 2000:
            k_2000 = count
        elif nominal == 1000:
            k_1000 = count
        elif nominal == 500:
            k_500 = count
        elif nominal == 100:
            k_100 = count
        elif nominal == 50:
            k_50 = count
        elif nominal == 10:
            k_10 = count
        elif nominal == 1:
            k_1 = count

# Вывод результатов
print("Количество купюр 5000 руб =", k_5000)
print("Количество купюр 2000 руб =", k_2000)
print("Количество купюр 1000 руб =", k_1000)
print("Количество купюр 500 руб =", k_500)
print("Количество купюр 100 руб =", k_100)
print("Количество купюр 50 руб =", k_50)
print("Количество купюр 10 руб =", k_10)
print("Количество купюр 1 руб =", k_1)
