def multiplicar(a,b):
    r=[]
    lr = len(a) + len(b) - 1
    for i in range(lr):
        r.append(0)

    for i in range(len(a)):
        for j in range(len(b)):
            r[i+j] += a[i] * b[j]
            
    return r 
            
            
x = [0, 1, 2, 3, 4]
y = [1, 0.9, -1, -2.3, 1.8]

c = multiplicar([1, -1], [1, -2])
print(c)
d = multiplicar(c, [1, -3])
print(d)

n = len(x)

      
    