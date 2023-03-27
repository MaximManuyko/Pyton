#Создать функцию calc(a, b, operation). Описание входных параметров:
#1. Первое число
#2. Второе число
#3. Действие над ними:
#   1) + Сложить
#   2) - Вычесть
#   3) * Умножить
#   4) / Разделить
#   5) В остальных случаях функция должна возвращать "Операция не поддерживается"

def calc(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return 'Деление на ноль невозможно'
        else:
            return a / b
    else:
        return 'Операция не поддерживается'

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
operation = input("Введите операцию (add, sub, mul, div): ")
print(calc(a, b, operation))



    # Проверяем корректные значения
print(calc(30, 15, '+'))
print(calc(30, 15, '-'))
print(calc(30, 15, '*'))
print(calc(30, 15, '/'))
    # Проверяем проверку деления на ноль
print(calc(30, 0, '/'))
    # Проверяем неподдерживаемую операцию
print(calc(30, 15, '%'))
