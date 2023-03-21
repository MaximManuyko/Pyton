#Реализуйте функцию fib(), находящую положительные Числа Фибоначчи. Аргументом функции является порядковый номер числа.
#
#Формула:
#
#f(0) = 0
#f(1) = 1
#f(n) = f(n-1) + f(n-2)
#fib(3)  # 2
#fib(5)  # 5
#fib(10)  # 55


            #code
def fib(number):
        f = [0, 1]
        for i in range(2, number +1):
            f.append(int(f[i - 2])+int(f[i - 1]))
        return f[number]


            # test
for a in range(0, 11):
    print(fib(a))