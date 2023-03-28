def sum_of_square_digits(number):
    sum_of_squares = 0
    for digit in str(number):
        digit_square = int(digit) ** 2
        sum_of_squares += digit_square

    return sum_of_squares    


# BEGIN (write your solution here)
def is_happy_number(number):
    """
    Принимает на вход число n и возвращает True, если оно является счастливым числом, и False — в противном случае.
    """
    for i in range(10):
        number = sum_of_square_digits(number)
        if number == 1:
            return True
    return False
# END

print(is_happy_number(7))