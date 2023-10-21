# Реализуйте функцию chunked, которая принимает на вход число и последовательность. Число задает размер чанка (куска). Функция должна вернуть список, состоящий из чанков указанной размерности. При этом список должен делиться на куски-списки, строка — на строки, кортеж — на кортежи!

# chunked(2, ['a', 'b', 'c', 'd'])  # [['a', 'b'], ['c', 'd']]
# chunked(3, ['a', 'b', 'c', 'd'])  # [['a', 'b', 'c'], ['d']]
# chunked(3, 'foobar')  # ['foo', 'bar']
# chunked(10, (42,))  # [(42,)]

def chunked(size, iterable):
    # Создаем пустой список для хранения чанков
    chunks = []

    if isinstance(iterable, (str, tuple)):
        # Если входной аргумент - строка или кортеж, разбиваем его на чанки
        for i in range(0, len(iterable), size):
            chunk = iterable[i:i + size]
            chunks.append(chunk)
    else:
        # Если входной аргумент - список или другой итерируемый объект, разбиваем его на чанки
        iterable = list(iterable)
        for i in range(0, len(iterable), size):
            chunk = iterable[i:i + size]
            chunks.append(chunk)

    return chunks
