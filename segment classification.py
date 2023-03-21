#В рамках этого испытания вы реализуете небольшой набор функций,
# работающих с отрезками прямых на двухмерной плоскости. 
#Отрезок в нашем случае будет кодироваться в виде пары пар и выглядеть как-то так: ((x1, y1), (x2, y2)) 
#(вложенные пары — это концы отрезка). Вам нужно реализовать четыре функции:

#is_degenerated() должна возвращать истину, если отрезок вырожден в точку (начало и конец совпадают);
#is_vertical() должна возвращать "истину", если отрезок — вертикальный;
#is_horizontal() должна возвращать "истину", если отрезок — горизонтальный;
#is_inclined() должна возвращать "истину", если отрезок — наклонный (не вертикальный и не горизонтальный).


#line1 = (0, 10), (100, 130)
#is_vertical(line1)  # False
#is_horizontal(line1)  # False
#is_degenerated(line1)  # False
#is_inclined(line1)  # True

#line2 = (42, 1), (42, 2)
#is_vertical(line2)  # True

#line3 = (100, 50), (200, 50)
#is_horizontal(line3)  # True

            #Info

#line = ((x1, y1), (x2, y2))
# x1 = line[0][0] y2 = line[0][1] x2 = line[1][0] y2 = [1][1]
            #code

def is_degenerated(line):
    return line[0] == line[1]
    

def is_vertical(line):
    if line[0] == line[1]:
        return False
    else:
        return line[0][0] == line[1][0]

def is_horizontal(line):
    if line[0] == line[1]:
        return False
    else:
        return line[0][1] == line[1][1]   

def is_inclined(line):
    return line[0][0] != line[1][0] and line[0][1] != line[1][1]



            #test

#line = (0, 10), (100, 130)
#print(is_vertical(line), False)  # False
#print(is_horizontal(line), False)  # False
#print(is_degenerated(line), False)  # False
#print(is_inclined(line), True)  # True

#line = (42, 100), (42, 100)
#print(is_vertical(line), True)  # True

line = (42, 100), (42, 100)
print(is_horizontal(line), True)  # True


