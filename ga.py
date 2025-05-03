import random
import math

# KONFIGURASI PARAMETER GA
POPULASI_SIZE = 30              # Jumlah kromosom dalam populasi
PANJANG_KROMOSOM = 16           # Panjang kromosom biner (8 bit untuk x1, 8 bit untuk x2)
X_MIN, X_MAX = -10, 10          # Domain nilai x1 dan x2
GENERASI_MAX = 100              # Jumlah generasi
PROB_CROSSOVER = 0.7            # Probabilitas crossover
PROB_MUTASI = 0.01              # Probabilitas mutasi per bit

random.seed(42)  # Menetapkan seed untuk hasil yang konsisten

# DEKODE KROMOSOM KE NILAI x1 dan x2
def decode_kromosom(kromosom):
    setengah = len(kromosom) // 2
    x1_bin = kromosom[:setengah]
    x2_bin = kromosom[setengah:]

    x1_int = int(x1_bin, 2)
    x2_int = int(x2_bin, 2)

    max_int = 2**setengah - 1
    x1 = X_MIN + (x1_int / max_int) * (X_MAX - X_MIN)
    x2 = X_MIN + (x2_int / max_int) * (X_MAX - X_MIN)

    return x1, x2

# FUNGSI OBJEKTIF (f(x1, x2)) SESUAI SOAL
def fungsi_objektif(x1, x2):
    try:
        return - (math.sin(x1) * math.cos(x2) * math.tan(x1 + x2) + (3/4) * math.exp(1 - math.sqrt(x1**2)))
    except:
        return float('inf') 

# HITUNG FITNESS UNTUK MINIMISASI
def hitung_fitness(kromosom):
    x1, x2 = decode_kromosom(kromosom)
    nilai = fungsi_objektif(x1, x2)
    return 1 / (1 + abs(nilai))

# OPERASI DASAR GENETIK
# Inisialisasi populasi awal secara acak
def inisialisasi_populasi():
    return [''.join(random.choice('01') for _ in range(PANJANG_KROMOSOM)) for _ in range(POPULASI_SIZE)]

# Seleksi turnamen (ambil yang terbaik dari k kandidat acak)
def seleksi_turnamen(populasi, k=3):
    kandidat = random.sample(populasi, k)
    kandidat.sort(key=hitung_fitness, reverse=True)
    return kandidat[0]