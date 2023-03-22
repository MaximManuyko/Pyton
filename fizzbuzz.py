#Реализуйте функцию fizz_buzz, которая возвращает строку с числами (через пробел) в диапазоне от begin до end включительно. 
#При этом:

#Если число делится без остатка на 3, то вместо него выводится слово Fizz
#Если число делится без остатка на 5, то вместо него выводится слово Buzz
#Если число делится без остатка и на 3, и на 5, то вместо числа выводится слово FizzBuzz
#В остальных случаях в строку добавляется само число
#Функция принимает два параметра (begin и end), определяющих начало и конец диапазона (включительно). Если диапазон пуст (в случае, когда begin > end), то функция возвращает пустую строку.

#Пример
#Вызов функции:

#from solution import fizz_buzz
#print(fizz_buzz(1, 5))
# => 1 2 Fizz 4 Buzz
#print(fizz_buzz(11, 20))
# => 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz

            #code
def fizz_buzz(start, end):
    t =''
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            t += ' FizzBuzz'
        elif i % 3 == 0:
            t += ' Fizz'
        elif i % 5 == 0:
            t += ' Buzz'
        
        else:
            t +=' ' + str(i)
    return t.strip()

            #test
            # 
print(fizz_buzz(1, 20))    

