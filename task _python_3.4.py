#Сложите цифры целого числа.

num = int(input("Введите число: "))
num_str = str(num)
sum = 0
for char in num_str:
    digit = int(char)
    sum += digit
print("Сумма цифр числа", num, "равна", sum)


#Выяснить, является ли строка палиндромом. 

def is_palindrome(string):
    string = string.replace(" ", "").lower()
    # Зеркальное отражение строки
    reverse_string = string[::-1]
    
    # Сравниваем символы строки с ее зеркальным отражением
    if string == reverse_string:
        return True
    else:
        return False
    
print(is_palindrome('Аргентина манит негра'))
print(is_palindrome('аргентина манит негра'))
print(is_palindrome('Манит Аргентина негра'))

#Дана строка из двух слов. Поменяйте слова местами. 

my_string = "снег идет"

# Разбиваем строку на список слов
words = my_string.split()
print(words)

# Меняем местами слова
reversed_words = words[::-1]
print(reversed_words)
# Объединяем слова в строку
result = ' '.join(reversed_words)

# Выводим результат
print(result)


my_string = "идет снег давно"

# Разбиваем строку на список слов
words = my_string.split()
print(words)

# Меняем местами слова
reversed_words = words[::-1]
print(reversed_words)
# Объединяем слова в строку
result = ' '.join(reversed_words)

# Выводим результат
print(result)