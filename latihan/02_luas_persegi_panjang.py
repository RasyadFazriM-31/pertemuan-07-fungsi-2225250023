# Latihan 2: Luas Persegi Panjang

def luas_persegi_panjang(p, l):
    return p * l


print(luas_persegi_panjang(8, 5))

# Test case: (input, hasil yang diharapkan)
test_case = [
    ((8, 5), 40),
    ((2.5, 4), 10),
    ((0, 7), 0),
]

print("--- Pengujian ---")
for (p, l), diharapkan in test_case:
    aktual = luas_persegi_panjang(p, l)
    status = "LULUS" if aktual == diharapkan else "GAGAL"
    print(f"p={p}, l={l} -> diharapkan {diharapkan}, aktual {aktual} [{status}]")
