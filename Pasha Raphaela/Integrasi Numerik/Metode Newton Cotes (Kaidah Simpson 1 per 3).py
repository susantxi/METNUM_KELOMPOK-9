def metode_simpson13(f, a, b, h):
    n = int((b - a) / h)
    
    if n % 2 != 0:
        print("Jumlah subinterval harus genap. Silakan masukkan nilai h yang sesuai.")
        return None

    integral = f(a) + f(b)

    # Menampilkan langkah-langkah perhitungan
    print("\nLangkah-langkah perhitungan:")
    print(f"{h}/3 * (f({a}) +", end="")

    for i in range(1, n):
        x = a + i * h
        koefisien = 4 if i % 2 == 1 else 2

        if i % 2 == 1:
            print(f" {koefisien} * f({x})", end="")
        else:
            print(f" {koefisien} * f({x})", end="")

        integral += koefisien * f(x)

    integral *= h / 3

    # Menampilkan hasil integral
    print(f" + f({b}))")
    print(f"\nHasil integral dari fungsi f(x) adalah {round(integral, 3)}")
    return integral

# Input dari pengguna
fungsi_input = input("Masukkan fungsi integrand-nya: ")
exec(f"def fungsi_integrand(x): return {fungsi_input}")

a_input = float(input("Masukkan batas awal interval a: "))
b_input = float(input("Masukkan batas akhir interval b: "))
h_input = float(input("Masukkan nilai h: "))

# Evaluasi fungsi dan hitung integral
hasil_integral_simpson13 = metode_simpson13(fungsi_integrand, a_input, b_input, h_input)