# ДНК и РНК это последовательности нуклеотидов.

# Четыре нуклеотида в ДНК:

# Аденин (A)
# Цитозин (C)
# Гуанин (G)
# Тимин (T)
# Четыре нуклеотида в РНК:

# Аденин (A)
# Цитозин (C)
# Гуанин (G)
# Урацил (U)
# Цепь РНК составляется на основе цепи ДНК последовательной заменой каждого нуклеотида:

# G -> C
# C -> G
# T -> A
# A -> U
# dna.py

# Напишите функцию to_rna, которая принимает на вход цепь ДНК и возвращает соответствующую цепь РНК (совершает транскрипцию РНК).

# import dna

# dna.to_rna('ACGTGGTCTTAA')
# # 'UGCACCAGAAUU'

def to_rna(dna_strand):
    rna_strand = ""
    for nucleotide in dna_strand:
        if nucleotide == 'G':
            rna_strand += 'C'
        elif nucleotide == 'C':
            rna_strand += 'G'
        elif nucleotide == 'T':
            rna_strand += 'A'
        elif nucleotide == 'A':
            rna_strand += 'U'
        else:
            # Если встретится некорректный нуклеотид, вы можете выбрать соответствующее действие.
            # В данном случае, я просто выведу ошибку.
            raise ValueError("Некорректный нуклеотид: " + nucleotide)
    return rna_strand


dna_sequence = 'ACGTGGTCTTAA'
rna_sequence = to_rna(dna_sequence)
print(rna_sequence)  # Выводит 'UGCACCAGAAUU'
