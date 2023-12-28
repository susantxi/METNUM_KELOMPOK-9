def metode_trapesium(f, a, b, h):
    n = int((b - a) / h)
    
    if n % 2 != 0:
        print("Jumlah subinterval harus genap. Silakan masukkan nilai h yang sesuai.")
        return None

    integral = f(a) + f(b)

    # Menampilkan langkah-langkah perhitungan
    print("Langkah-langkah perhitungan:")
    print(f"{h}/2 * (f({a})", end="")

    for i in range(1, n):
        x = a + i * h
        integral += 2 * f(x)
        print(f" + 2 * f({x})", end="")

    integral *= h / 2

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
hasil_integral = metode_trapesium(fungsi_integrand, a_input, b_input, h_input)