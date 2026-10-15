# Latihan 3: Jumlah 1 sampai n

def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def jumlah_rumus(n):
    # Rumus deret aritmetika: n(n+1)/2
    return n * (n + 1) // 2


print(jumlah_n(10))

print("--- Perbandingan perulangan dengan rumus n(n+1)/2 ---")
for n in [1, 5, 10, 100]:
    hasil_loop = jumlah_n(n)
    hasil_rumus = jumlah_rumus(n)
    status = "SAMA" if hasil_loop == hasil_rumus else "BEDA"
    print(f"n={n}: perulangan={hasil_loop}, rumus={hasil_rumus} [{status}]")
