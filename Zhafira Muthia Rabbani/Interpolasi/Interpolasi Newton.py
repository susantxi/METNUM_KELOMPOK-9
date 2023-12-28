def newton_interpolation(points):
    n = len(points)
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    def divided_differences(x, y, n):
        table = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            table[i][0] = y[i]

        for j in range(1, n):
            for i in range(n - j):
                table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])

        return table

    def newton_polynomial(x_input, x, differences):
        result = differences[0][0]
        term = 1
        for i in range(1, n):
            term *= (x_input - x[i - 1])
            result += differences[0][i] * term

        return result

    differences = divided_differences(x, y, n)

    return newton_polynomial, differences

def print_newton_interpolation(points, coefficients):
    n = len(points)
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    print("Polinom Interpolasi Newton:")
    polynomial = f"P(x) = {coefficients[0][0]}"
    for i in range(1, n):
        polynomial += f" + {coefficients[0][i]}"
        for j in range(i):
            polynomial += f" * (x - {x[j]})"
    print(polynomial)

# Meminta pengguna untuk memasukkan jumlah pasangan titik
n = int(input("Masukkan jumlah titik data: "))
points = []

for i in range(n):
    x = float(input(f"Masukkan x_{i}: "))
    y = float(input(f"Masukkan y_{i}: "))
    points.append((x, y))

# Membuat fungsi interpolasi Newton
newton_interpolation_function, differences = newton_interpolation(points)

# Meminta pengguna untuk memasukkan nilai x yang ingin dicari
x_input = float(input("Masukkan nilai x untuk mencari y: "))

# Menghitung y menggunakan interpolasi Newton
y_output = newton_interpolation_function(x_input, [point[0] for point in points], differences)

print(f"Nilai y yang sesuai dengan x = {x_input} adalah {y_output}")

# Menampilkan polinom interpolasi Newton
print_newton_interpolation(points, differences)