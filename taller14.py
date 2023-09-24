def gauss_jordan(ec):
    n = len(ec)
    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(ec[j][i]) > abs(ec[max_row][i]):
                max_row = j
        ec[i], ec[max_row] = ec[max_row], ec[i]
        # Scale pivot row
        pivote = ec[i][i]
        for j in range(i, n + 1):
            ec[i][j] /= pivote
        # Eliminate other rows
        for j in range(n):
            if i == j:
                continue
            factor = ec[j][i]
            for k in range(i, n + 1):
                ec[j][k] -= factor * ec[i][k]
    return [row[-1] for row in ec]

ec = [[1, 1, 0, 5], [3, 3, 4, 23], [4, 0, 1, 30]]
valores = gauss_jordan(ec)

print(valores)









