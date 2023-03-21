i = 100000
t = 0
while i < 1000000:
    if int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) == int(str(i)[3]) + int(str(i)[4]) + int(str(i)[5]):
        t += 1
    i += 1
print(t)        
