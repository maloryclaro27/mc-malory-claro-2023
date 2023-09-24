x = 0
def conjuntos(cantidad_a, cantidad_b, elemento, elemento_b):
    cantidad_a = int(input("Número de elementos del conjunto A: "))
    cantidad_b = int(input("Número de elementos del conjunto B: "))
    print("")
    
    a = set()
    for i in range(cantidad_a):
        elemento = int(input("Ingrese un elemento para el conjunto A: "))
        a.add(elemento)
        return a
        print("")
    b = set()
    for i in range(cantidad_b):
        elemento_b = int(input("Ingrese un elemento para el conjunto B: "))
        b.add(elemento_b)
        return b

while x == 0:
    print(f'Operaciones con conjuntos: Escoge una opción \n\
      1. Unión \n\
      2. Intersección \n\
      3. Diferencia \n\
      4. Diferencia simétrica \n\
      5. Salir ')
    opcion = int(input("Selección: "))
    print("")

    if opcion == 1:
        def conjuntos(cantidad_a, cantidad_b, elemento, elemento_b)
        print("A U B = ", a | b)
    elif opcion == 2:
        cantidad_a = int(input("Número de elementos del conjunto A: "))
        cantidad_b = int(input("Número de elementos del conjunto B: "))
        print("")

        a = set()
        for i in range(cantidad_a):
            elemento = int(input("Ingrese un elemento para el conjunto A: "))
            a.add(elemento)
        print("A = ", a)
        print("")
        b = set()
        for i in range(cantidad_b):
            elemento_b = int(input("Ingrese un elemento para el conjunto B: "))
            b.add(elemento_b)
        print("B = ", b)
        print("")
        print("A & B = ", a & b)
    elif opcion == 3:
        cantidad_a = int(input("Número de elementos del conjunto A: "))
        cantidad_b = int(input("Número de elementos del conjunto B: "))
        print("")

        a = set()
        for i in range(cantidad_a):
            elemento = int(input("Ingrese un elemento para el conjunto A: "))
            a.add(elemento)
        print("A = ", a)
        print("")
        b = set()
        for i in range(cantidad_b):
            elemento_b = int(input("Ingrese un elemento para el conjunto B: "))
            b.add(elemento_b)
        print("B = ", b)
        print("")
        print("A - B = ", a - b)
    elif opcion == 4:
        cantidad_a = int(input("Número de elementos del conjunto A: "))
        cantidad_b = int(input("Número de elementos del conjunto B: "))
        print("")

        a = set()
        for i in range(cantidad_a):
            elemento = int(input("Ingrese un elemento para el conjunto A: "))
            a.add(elemento)
        print("A = ", a)
        print("")
        b = set()
        for i in range(cantidad_b):
            elemento_b = int(input("Ingrese un elemento para el conjunto B: "))
            b.add(elemento_b)
        print("B = ", b)
        print("")
        print("A ^ B = ", a ^ b)
    else: 
        break

