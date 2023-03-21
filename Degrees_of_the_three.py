#Реализуйте функцию is_power_of_three(), которая определяет, является ли переданное число натуральной степенью тройки. 
#Например, число 27 — это третья степень: 3 ** 3, а 81 — это четвёртая: 3 ** 4.

#Пример:

#is_power_of_three(1)  # True
#is_power_of_three(2)  # False
#is_power_of_three(9)  # True

            #code

#def is_power_of_three(n):
#    if n < 1:
#        return False
#    while n % 3 == 0:
#        n //= 3
#    return n == 1


def is_power_of_three(number):
    i = 1
    while i < number:
        i *=3
    return i == number




print(is_power_of_three(12))
