# Реализуйте функцию hamming_weight, которая считает вес Хэмминга.

# Примеры
# hamming_weight(0)  # 0
# hamming_weight(4)  # 1
# hamming_weight(101)  # 4

# Вес Хэмминга — величина, использующаяся в криптографии и теории кодирования информации. 

def hamming_weight(number):
    weight = 0
    while number > 0:
        # Проверяем крайний бит числа
        weight += number & 1
        # Сдвигаем число вправо, отбрасывая младший бит
        number >>= 1
    return weight

# Примеры использования:

print(hamming_weight(0))     # 0
print(hamming_weight(4))     # 1
print(hamming_weight(101))   # 4
