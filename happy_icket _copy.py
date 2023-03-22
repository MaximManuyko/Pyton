#"Счастливым" называют билет с номером, в котором сумма первой половины цифр равна сумме второй половины цифр. 
#Номера могут быть произвольной длины, с единственным условием, что количество цифр всегда чётно, например: 33 или 2341
# и так далее.

#Билет с номером 385916 — счастливый, так как 3 + 8 + 5 == 9 + 1 + 6. Билет с номером 231002 не является счастливым,
# так как 2 + 3 + 1 != 0 + 0 + 2.

#src/solution.py

#Реализуйте функцию is_happy_ticket(), проверяющую является ли номер счастливым (номер — всегда строка). 
#Функция должна возвращать True, если билет счастливый, или False, если нет.

#Примеры использования:

#is_happy_ticket('123123') # True
#is_happy_ticket('341800') # True

#is_happy_ticket('42') # False
#is_happy_ticket('12345678') # False


            #code

def is_happy_ticket(number):
    digits = [int(d) for d in str(number)]
    length = len(digits)
    half = length // 2
    first = digits[:half]
    second = digits[half:]
    if sum(first) == sum(second):
        t = True
    else:
        t = False
    return t






            #test
text = input("Введите число: ") 
is_happy_ticket(text)

