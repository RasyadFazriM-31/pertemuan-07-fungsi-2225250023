# Latihan 5: Eksperimen Scope

# Prediksi keluaran (ditulis sebelum menjalankan):
#   di dalam fungsi: 20 25
#   di luar fungsi: 10 25

x = 10  # variabel global


def demo(x):  # x di sini adalah parameter, variabel LOKAL yang berbeda dari x global
    y = x + 5
    print("di dalam fungsi:", x, y)
    return y


hasil = demo(20)
print("di luar fungsi:", x, hasil)

# Penjelasan:
# Saat demo(20) dipanggil, parameter x menerima nilai 20. Parameter ini hanya
# ada di local scope fungsi demo, sehingga ia menutupi (shadow) x global selama
# fungsi berjalan. Perhitungan y = 20 + 5 = 25 memakai x lokal tersebut.
# Setelah fungsi selesai, x lokal hilang. Variabel x global tidak pernah
# diubah, jadi nilainya tetap 10. Variabel y juga lokal; nilainya hanya
# sampai ke luar karena dikembalikan lewat return dan disimpan di "hasil".
