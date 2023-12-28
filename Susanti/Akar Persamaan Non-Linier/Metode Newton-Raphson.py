# Metode Newton-Raphson untuk mencari akar f(x)
def newtonRaphson(x0, e, N, f, g):
    step = 1  # Inisialisasi langkah awal
    flag = 1  # Penanda jika metode konvergen
    condition = True  # Kondisi iterasi dimulai

    while condition:
        if g(x0) == 0.0:
            print('Terjadi pembagian oleh 0.')
            break

        # Iterasi Newton-Raphson
        x1 = x0 - f(x0) / g(x0)
        print('Iterasi-%d, x1 = %0.6f dan f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step += 1

        # Berhenti jika langkah melebihi N atau error sudah mencukupi
        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    # Hasil akhir
    if flag == 1:
        print('\nAkar yang ditemukan: %0.8f' % x1)
    else:
        print('\nMetode tidak konvergen')

# Input fungsi dari pengguna
fungsi_f = input("Masukkan fungsi f(x): ")
f = lambda x: eval(fungsi_f)

fungsi_g = input("Masukkan fungsi f'(x): ")
g = lambda x: eval(fungsi_g)

# Input dari pengguna
x0 = float(input('Masukkan perkiraan awal: '))
e = float(input('Masukkan tingkat toleransi: '))
N = int(input('Masukkan jumlah iterasi maksimal: '))

# Menjalankan metode Newton-Raphson
newtonRaphson(x0, e, N, f, g)