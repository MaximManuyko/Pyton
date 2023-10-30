sum_input = float(input("Введите сумму(Руб.): "))  # Запрашиваем ввод суммы у пользователя

if sum_input <= 0 or not sum_input.is_integer():
    print("Пожалуйста, введите положительное целое число.")
else:
    sum_input = int(sum_input)  # Convert the input to an integer
    print("Сумма: " + str(sum_input) + " руб.")  # Выводим сумму до обработки, потому что после цикла переменная изменится на ноль

    nominals = [5000, 2000, 1000, 500, 100, 50, 10, 1]  # Список номиналов купюр

    k_5000, k_2000, k_1000, k_500, k_100, k_50, k_10, k_1 = 0, 0, 0, 0, 0, 0, 0, 0  # Инициализируем переменные для подсчета количества купюр каждого номинала

    for nominal in nominals:  # Обрабатываем введенную сумму и подсчитываем количество каждого номинала
        if sum_input >= nominal:
            count = int(sum_input // nominal)
            sum_input -= count * nominal

            if nominal == 5000:  # Сохраняем количество каждого номинала
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

    if k_5000 > 0:  # Выводим количество купюр, только если их количество больше нуля
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
