import numpy as np  # Mengimpor pustaka NumPy

# Definisi fungsi bisection untuk mencari akar
def bisection_method(f, a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("Tidak ada perubahan tanda f(a) dan f(b). Metode ini tidak berlaku.")
        return None
            
    iteration = 0
    while iteration < max_iter and (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteration += 1
        
    return c

# Input fungsi dari pengguna
fungsi = input("Masukkan fungsi f(x): ")
f = lambda x: eval(fungsi)

# Input interval serta tingkat toleransi
a = float(input("Masukkan batas awal interval a: "))
b = float(input("Masukkan batas akhir interval b: "))
toleransi = float(input("Masukkan tingkat toleransi: "))

# Input jumlah iterasi maksimal
maksimal_iterasi = int(input("Masukkan jumlah iterasi maksimal: "))

# Panggil fungsi bisection_method untuk mencari akar
akar = bisection_method(f, a, b, toleransi, maksimal_iterasi)

# Cetak hasil
if akar is not None:
    print(f"Akar dari fungsi adalah {akar:.3f}")
    print(f"f(m)                : {f(akar):.3f}")
else:
    print("Metode bagi dua tidak konvergen dalam iterasi yang diberikan.")