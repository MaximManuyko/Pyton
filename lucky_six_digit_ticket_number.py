i = 100000
t = 0
while i <= 999999:
    z = str(i)
    a = int(z[0])
    b = int(z[1])
    c = int(z[2])
    d = int(z[3])
    e = int(z[4])
    f = int(z[5])
    #print(a+b+c,d+e+f)
    #print(z)
    if a + b + c == d + e + f:
        t += 1
        print(i, t)
    
    i += 1
print(t)