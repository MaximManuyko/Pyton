#В этом испытании вы будете работать с "тройками" — кортежами из трёх элементов. Вам предстоит реализовать две функции, которые "вращают" тройку влево и вправо. Как это выглядит, вы можете понять из пары примеров:

#triple = ('A', 'B', 'C')
#rotate_left(triple)  # ('B', 'C', 'A')
#rotate_right(triple)  # ('C', 'A', 'B')

            #code

def rotate_left(triple):
    return triple[1], triple[2], triple[0]

def rotate_right(triple):
    return triple[2], triple[0], triple[1]


            #test

triple = ('A', 'B', 'C')
print(rotate_left(triple))    
print(rotate_right(triple))