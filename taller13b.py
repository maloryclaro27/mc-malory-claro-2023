def main():
    fila_A = int(input("Ingrese el número de filas de la matriz A: "))
    columna_A = int(input("Ingrese el número de columnas de la matriz A: "))

    fila_B = int(input("Ingrese el número de filas de la matriz B: "))
    columna_B = int(input("Ingrese el número de columnas de la matriz B: "))

    if fila_A != fila_B or columna_A != columna_B:
        print("Las matrices no son compatibles para las operaciones.")
        return

    matriz_A = crear_matriz(fila_A, columna_A)
    matriz_B = crear_matriz(fila_B, columna_B)

    while True:
        print("\nMenú de Operaciones:")
        print("a) 3A")
        print("b) 4B")
        print("c) A + B")
        print("d) B × A")
        print("e) Salir")

        opcion = input("Seleccione una opción (a/b/c/d/e): ")

        if opcion == 'a':
            resultado = escalar_matriz(matriz_A, 3)
            imprimir_matriz("3A =", resultado)
        elif opcion == 'b':
            resultado = escalar_matriz(matriz_B, 4)
            imprimir_matriz("4B =", resultado)
        elif opcion == 'c':
            resultado = suma_matrices(matriz_A, matriz_B)
            imprimir_matriz("A + B =", resultado)
        elif opcion == 'd':
            resultado = multiplicar_matrices(matriz_B, matriz_A)
            imprimir_matriz("B × A =", resultado)
        elif opcion == 'e':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def crear_matriz(filas, columnas):
    matriz = []
    print(f"Ingrese los elementos de la matriz ({filas}x{columnas}):")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"Elemento ({i+1},{j+1}): "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz

def escalar_matriz(matriz, escalar):
    return [[elemento * escalar for elemento in fila] for fila in matriz]

def suma_matrices(matriz_A, matriz_B):
    return [[matriz_A[i][j] + matriz_B[i][j] for j in range(len(matriz_A[0]))] for i in range(len(matriz_A))]

def multiplicar_matrices(matriz_B, matriz_A):
    return [[sum(matriz_B[i][k] * matriz_A[k][j] for k in range(len(matriz_B[0]))) for j in range(len(matriz_A[0]))] for i in range(len(matriz_B))]

def imprimir_matriz(mensaje, matriz):
    print(mensaje)
    for fila in matriz:
        print(" ".join(str(round(elemento, 2)) for elemento in fila))

if __name__ == "__main__":
    main()












