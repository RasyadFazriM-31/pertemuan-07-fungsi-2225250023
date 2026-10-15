# Latihan 4: Statistik Sederhana
# Satu fungsi dapat mengembalikan beberapa nilai sekaligus (tuple).

def statistik(data):
    total = 0
    minimum = data[0]
    maksimum = data[0]
    for x in data:
        total += x
        if x < minimum:
            minimum = x
        if x > maksimum:
            maksimum = x
    rata = total / len(data)
    return minimum, maksimum, rata


mn, mx, rt = statistik([70, 80, 65, 90, 75])
print(mn, mx, rt)

print("--- Pengujian ---")
test_case = [
    ([70, 80, 65, 90, 75], (65, 90, 76.0)),
    ([5], (5, 5, 5.0)),
    ([3, 3, 3], (3, 3, 3.0)),
    ([-2, 0, 2], (-2, 2, 0.0)),
]
for data, diharapkan in test_case:
    aktual = statistik(data)
    status = "LULUS" if aktual == diharapkan else "GAGAL"
    print(f"{data} -> diharapkan {diharapkan}, aktual {aktual} [{status}]")
