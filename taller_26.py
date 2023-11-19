class NodoBPlus:
    def __init__(self, hoja=True):
        self.claves = []
        self.hijos = []
        self.hoja = hoja
        self.siguiente = None  

def insertar_arbol_bplus(raiz, valor, m):
    if raiz is None:
        return NodoBPlus(hoja=True, claves=[valor])

    if raiz.hoja:
        raiz.claves.append(valor)
        raiz.claves.sort()

        if len(raiz.claves) > m:
            nueva_raiz = NodoBPlus(hoja=True)
            nueva_raiz.claves = raiz.claves[m // 2:]
            raiz.claves = raiz.claves[:m // 2]
            nueva_raiz.siguiente = raiz.siguiente
            raiz.siguiente = nueva_raiz
            return nueva_raiz

    else:
        i = 0
        while i < len(raiz.claves) and valor > raiz.claves[i]:
            i += 1

        raiz.hijos[i] = insertar_arbol_bplus(raiz.hijos[i], valor, m)

        if len(raiz.hijos[i].claves) > m:
            nueva_raiz = NodoBPlus(hoja=False)
            nueva_raiz.claves = raiz.hijos[i].claves[m // 2:]
            raiz.hijos[i].claves = raiz.hijos[i].claves[:m // 2]
            nueva_raiz.hijos = [raiz.hijos[i]]
            raiz.hijos[i] = nueva_raiz
            return raiz

    return raiz

def recorrer_arbol_bplus(raiz):
    if raiz:
        for i in range(len(raiz.claves)):
            recorrer_arbol_bplus(raiz.hijos[i])
            print(raiz.claves[i], end=' ')
        recorrer_arbol_bplus(raiz.siguiente)

conjunto_A = [21, 14, 2, 11, 7, 20, 13, 30, 18, 5, 6, 29, 12, 27, 4, 28, 10, 15, 22, 1, 19, 3]

m = 5

raiz_arbol_bplus = None

for elemento in conjunto_A:
    raiz_arbol_bplus = insertar_arbol_bplus(raiz_arbol_bplus, elemento, m)

print("Árbol B+:")
recorrer_arbol_bplus(raiz_arbol_bplus)
