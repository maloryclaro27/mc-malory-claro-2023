class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def insertar_nodo(raiz, valor):
    if raiz is None:
        return Nodo(valor)
    else:
        if valor < raiz.valor:
            raiz.izquierda = insertar_nodo(raiz.izquierda, valor)
        elif valor > raiz.valor:
            raiz.derecha = insertar_nodo(raiz.derecha, valor)
    return raiz

def recorrer_inorden(raiz):
    if raiz:
        recorrer_inorden(raiz.izquierda)
        print(raiz.valor, end=' ')
        recorrer_inorden(raiz.derecha)

conjunto_A = [21, 14, 2, 11, 7, 20, 13, 30, 18, 5, 6, 29, 12, 27, 4, 28, 10, 15, 22, 1, 19, 3]

raiz_arbol = None

for elemento in conjunto_A:
    raiz_arbol = insertar_nodo(raiz_arbol, elemento)

print("Recorrido inorden del árbol:")
recorrer_inorden(raiz_arbol)

