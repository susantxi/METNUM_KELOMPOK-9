def metode_titik_tengah(f, a, b, h):
    n = int((b - a) / h)
    integral = 0

    # Menampilkan langkah-langkah perhitungan
    print("Langkah-langkah perhitungan:")
    print(f"{h} * (", end="")

    for i in range(n):
        x_mid = (a + i * h + a + (i + 1) * h) / 2
        integral += f(x_mid)
        print(f"f({x_mid})", end="")
        if i < n - 1:
            print(" + ", end="")

    integral *= h

    # Menampilkan hasil integral
    print(")")
    print(f"\nHasil integral dari fungsi f(x) adalah {round(integral, 3)}")
    return integral

# Input dari pengguna
fungsi_input = input("Masukkan fungsi integrand-nya: ")
exec(f"def fungsi_integrand(x): return {fungsi_input}")

a_input = float(input("Masukkan batas awal interval a: "))
b_input = float(input("Masukkan batas akhir interval b: "))
h_input = float(input("Masukkan nilai h: "))

# Evaluasi fungsi dan hitung integral
hasil_integral = metode_titik_tengah(fungsi_integrand, a_input, b_input, h_input)