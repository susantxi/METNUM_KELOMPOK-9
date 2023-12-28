def gauss_elimination(A, b):
    n = len(b)

    # Eliminasi maju (forward elimination)
    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]

    # Cek apakah baris terakhir merupakan baris nol
    if A[n - 1][n - 1] == 0 and b[n - 1] == 0:
        print("SPL memiliki solusi banyak.")
        return None
    elif A[n - 1][n - 1] == 0 and b[n - 1] != 0:
        print("SPL tidak memiliki solusi.")
        return None

    # Substitusi mundur (backward substitution)
    x = [0] * n
    for k in range(n - 1, -1, -1):
        x[k] = b[k]
        for j in range(k + 1, n):
            x[k] -= A[k][j] * x[j]
        x[k] /= A[k][k]

    return x

# Masukkan jumlah persamaan
n = int(input("Jumlah Persamaan: "))

# Masukkan koefisien SPL (matriks A)
A = []
print("Masukkan Koefisien Matriks A: ")
for i in range(n):
    row = []
    for j in range(n):
        row.append(float(input(f"A[{i + 1}],[{j + 1}]: ")))
    A.append(row)

# Masukkan vektor hasil (matriks b)
b = []
print("Masukkan Vektor Hasil b: ")
for i in range(n):
    b.append(float(input(f"b[{i + 1}]: ")))

# Memanggil fungsi gauss_elimination untuk menyelesaikan SPL
solusi = gauss_elimination(A, b)

# Menampilkan solusi SPL
if solusi is not None:
    print("Solusi SPL: ")
    for i in range(n):
        print(f"x[{i + 1}] = {solusi[i]}")