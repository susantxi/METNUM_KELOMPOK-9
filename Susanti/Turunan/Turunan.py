def interpolasi_newton(nilai_x, nilai_y, x):
    n = len(nilai_x)
    F = [[0] * n for _ in range(n)]

    for i in range(n):
        F[i][0] = nilai_y[i]

    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (nilai_x[i + j] - nilai_x[i])

    result = F[0][0]

    for j in range(1, n):
        term = F[0][j]
        for i in range(j):
            term *= (x - nilai_x[i])
        result += term
    return result

def hitung(f, x, h, turunan, metode):
    if turunan == 1:
        if metode == 1:
            return (f(x + h) - f(x)) / h
        elif metode == 2:
            return (f(x) - f(x - h)) / h
        elif metode == 3:
            return (f(x + h) - f(x - h)) / (2 * h)
        else:
            print("Metode tidak valid.")
            return None
    elif turunan == 2:
        if metode == 1:
            return (f(x + 2 * h) - 2 * f(x + h) + f(x)) / h**2
        elif metode == 2:
            return (f(x) - 2 * f(x - h) + f(x - 2 * h)) / h**2
        elif metode == 3:
            return (f(x + h) - 2 * f(x) + f(x - h)) / h**2
        else:
            print("Metode tidak valid.")
            return None
    else:
        print("")
        return None

def main():
    jumlah_titik_data = int(input("Masukkan jumlah titik data: "))
    nilai_x = []
    nilai_y = []
    
    for i in range(jumlah_titik_data):
        nilai_x.append(float(input(f"Masukkan x{i + 1}: ")))
        nilai_y.append(float(input(f"Masukkan f(x){i + 1}: ")))

    x = float(input("Masukkan nilai x: "))

    print("Metode:")
    print("1. Selisih Maju")
    print("2. Selisih Mundur")
    print("3. Selisih Pusat")
    metode = int(input("Pilih metode yang ingin digunakan: "))

    h = float(input("Masukkan nilai h: "))

    f = lambda x: interpolasi_newton(nilai_x, nilai_y, x)

    turunan = int(input("Pilih turunan yang ingin dicari (1 atau 2): "))

    hasil = hitung(f, x, h, turunan, metode)

    if hasil is not None:
        formatted_result = "{:.3f}".format(hasil)
        if metode == 1:
            print(f"Nilai turunan ke-{turunan} menggunakan metode Selisih Maju: {formatted_result}")
        elif metode == 2:
            print(f"Nilai turunan ke-{turunan} menggunakan metode Selisih Mundur: {formatted_result}")
        elif metode == 3:
            print(f"Nilai turunan ke-{turunan} menggunakan metode Selisih Pusat: {formatted_result}")
        else:
            print("Metode tidak valid.")

if __name__ == "__main__":
    main()