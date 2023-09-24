def inversa(matriz):
    n = len(matriz)
    inversa = [[0] * n for i in range(n)]
    for i in range(n):
        inversa[i][i] = 1
    for i in range(n):
        factor = matriz[i][i]
        for j in range(n):
            matriz[i][j] /= factor
            inversa[i][j] /= factor
        for j in range(n):
            if i == j:
                continue
            factor = matriz[j][i]
            for k in range(n):
                matriz[j][k] -= factor * matriz[i][k]
                inversa[j][k] -= factor * inversa[i][k]
    return inversa

matriz = [[1, 2, 0, 4], [2, 0, -1, -2], [1, 1, -1, 0], [0, 4, 1, 0]]
inversa = inversa(matriz)

print(inversa)









