def lagrange_interpolation(points):
    n = len(points)

    def l_k(k, x):
        result = 1
        x_k, y_k = points[k]
        for i in range(n):
            if i != k:
                x_i, _ = points[i]
                result *= (x - x_i) / (x_k - x_i)
        return result

    def lagrange(x):
        result = 0
        for k in range(n):
            x_k, y_k = points[k]
            result += y_k * l_k(k, x)
        return result

    return lagrange

# Meminta pengguna untuk memasukkan jumlah pasangan titik
n = int(input("Jumlah pasangan titik: "))
points = []

for i in range(n):
    x = float(input(f"Masukkan x_{i}: "))
    y = float(input(f"Masukkan y_{i}: "))
    points.append((x, y))

# Membuat fungsi interpolasi Lagrange
lagrange_function = lagrange_interpolation(points)

# Meminta pengguna untuk memasukkan nilai x yang ingin dicari
x_input = float(input("Masukkan nilai x untuk mencari y: "))

# Menghitung y menggunakan polinom Lagrange
y_output = lagrange_function(x_input)

print(f"Nilai y yang sesuai dengan x = {x_input} adalah {y_output}")

def print_lagrange_interpolation(points):
    n = len(points)
    lagrange_interpolation = []

    for k in range(n):
        x_k, y_k = points[k]
        term = f"({y_k:.4f})"

        for i in range(n):
            if i != k:
                x_i, _ = points[i]
                term = f"{term} * (x - {x_i:.1f}) / ({x_k:.1f} - {x_i:.1f})"

        if k < n - 1:
            term += " + "

        lagrange_interpolation.append(term)

    print("Polinom Interpolasi Lagrange:")
    for term in lagrange_interpolation:
        print(term)

# Menampilkan polinom interpolasi Lagrange
print_lagrange_interpolation(points)