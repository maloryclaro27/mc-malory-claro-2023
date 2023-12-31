import math

def coseno(x):
    
    x = math.radians(x)
    
    cos_x = 1
    n = 2
    epsilon = 0.00000001  # Criterio de error esperado con ocho cifras significativas
    iteraciones = 0
    
    while True:
        termino = ((-1) ** (n // 2)) * (x ** n) / math.factorial(n)
        if abs(termino) < epsilon:
            break
        cos_x += termino
        n += 2
        iteraciones += 1
    
    cos_exacto = math.cos(x)
    error_aproximado = abs(cos_exacto - cos_x)
    error_relativo = (error_aproximado / abs(cos_exacto)) * 100
    
    print(f"El valor estimado del coseno de {x} es {cos_x:.8f}")
    print(f"El error aproximado relativo porcentual es {error_relativo:.8f}%")
    print(f"El número de iteraciones realizadas es {iteraciones}")

x = float(input("Ingrese un angulo en grados: "))

coseno(x)


