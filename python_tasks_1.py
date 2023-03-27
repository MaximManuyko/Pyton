#Создать произвольный список
import random

random_list = [random.randint(0, 100) for item in range(50)]
print(random_list)

#Добавить новый элемент типа str в конец списка

new_str = 'Hallo'
random_list.append(new_str)
print(random_list)

#Добавить новый элемент типа int на место с индексом

new_int = 69
random_list.insert(20, new_int)
print(random_list)

#Добавить новый элемент типа list в конец списка

new_list = [1000, 2000, 3000]
random_list.append(new_list)
print(random_list)

#Добавить новый элемент типа tuple на место с индексом

new_tuple = (11111, 2222, 3333)
random_list.insert(15, new_tuple)
print(random_list)

#Получить элемент по индексу

print(random_list[16])

#Удалить элемент

del random_list[11]
print(random_list)

#Найти число повторений элемента списка

count = random_list.count([5])
print("Число повторений элемента", random_list[5], "в списке: ", count)

#Получите первый и последний элемент списка

first_element = random_list[0]
last_element = random_list[-1]
print("Первый элемент списка: ", first_element)
print("Последний элемент списка: ", last_element)

#Поменяйте значения переменных a и b местами и обратно

temp = first_element
first_element = last_element
last_element = temp
print("Первый элемент списка: ", first_element)
print("Последний элемент списка: ", last_element)
first_element, last_element = last_element, first_element
print("Первый элемент списка: ", first_element)
print("Последний элемент списка: ", last_element)

#Проверить, есть ли в последовательности дубликаты

random_list = [random.randint(0, 100) for item in range(50)]
print(random_list)
if len(set(random_list)) < len(random_list):
    print("В списке есть дубликаты.")
else:
    print("В списке нет дубликатов.")