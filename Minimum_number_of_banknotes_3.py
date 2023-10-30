# Задача на выдачу минимального количество купюр с проверкой ввода только целого положительного числа,
# выводом купюр количество, которых больше нуля и возможностью продолжения цикла, если вводиться целое положительное число
# Функция для проверки, является ли ввод целым числом больше нуля
def is_positive_integer(value):
    return value.isdigit() and int(value) > 0

while True:
    first_iteration = True
    sum_input = input("Введите сумму(Руб.): ")

    while is_positive_integer(sum_input):
        sum_input = int(sum_input)
        nominals = [5000, 2000, 1000, 500, 100, 50, 10, 1]

        k_5000 = 0
        k_2000 = 0
        k_1000 = 0
        k_500 = 0
        k_100 = 0
        k_50 = 0
        k_10 = 0
        k_1 = 0

        for nominal in nominals:
            while sum_input >= nominal:
                count = sum_input // nominal
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

        if k_5000 > 0:
            print("Количество купюр 5000 руб =", k_5000)
        if k_2000 > 0:
            print("Количество купюр 2000 руб =", k_2000)
        if k_1000 > 0:
            print("Количество купюр 1000 руб =", k_1000)
        if k_500 > 0:
            print("Количество купюр 500 руб =", k_500)
        if k_100 > 0:
            print("Количество купюр 100 руб =", k_100)
        if k_50 > 0:
            print("Количество купюр 50 руб =", k_50)
        if k_10 > 0:
            print("Количество купюр 10 руб =", k_10)
        if k_1 > 0:
            print("Количество купюр 1 руб =", k_1)

        first_iteration = False  # Первая итерация завершена
        sum_input = input("Введите сумму(Руб.): ")

    if not first_iteration:
        break  # Завершаем выполнение, если ввод не соответствует требованиям после первой итерации
