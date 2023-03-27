#1. Создать произвольный словарь
my_dict = {'apple': 3, 'banana': 2, 'orange': 5, 'grape': 1}
print(my_dict)

#2. Добавить новый элемент с ключом типа str и значением типа int 

my_dict['kiwi'] = 2
print(my_dict)

#3. Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list)

my_key = (1, 2, 3)
my_value = [4, 5, 6]
my_dict[my_key] = my_value
print(my_dict)

#4. Получить элемент по ключу

print(my_dict['banana'])

#5. Удалить элемент по ключу

del my_dict['orange']
print(my_dict)

#Получить список ключей словаря

keys_list = list(my_dict.keys())
print(keys_list)

#1. Создать множество(set) 

my_set = {1, 2, 3}
print(my_set) # выведет {1, 2, 3}

#2. Создать неизменяемое множество(frozenset) 

my_frozenset = frozenset([6, 7, 8])
print(my_frozenset) # выведет frozenset({1, 2, 3})

#3. Выполнить операцию объединения созданных множеств

union_set = my_set | my_frozenset
print(union_set)

#4. Выполнить операцию пересечения созданных множеств my_set   my_frozenset

my_set = {1, 2, 3, 4}
my_frozenset = frozenset([3, 4, 5, 6])
intersection_set = my_set & my_frozenset
print(intersection_set) # выведет {3, 4}
