# Praktik 2: Utilitas Matematika Modular
# Perhitungan ada di fungsi (parameter + return), interaksi pengguna ada di program utama.


def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def faktorial(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil


def nonnegatif(n):
    # True jika n adalah bilangan bulat nonnegatif
    return isinstance(n, int) and n >= 0


def tampilkan_menu():
    print("=== Utilitas Matematika ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")


def baca_angka(pesan):
    # Mengembalikan float, atau None jika masukan bukan angka
    try:
        return float(input(pesan))
    except ValueError:
        return None


def baca_bilangan_bulat(pesan):
    # Mengembalikan int, atau None jika masukan bukan bilangan bulat
    try:
        return int(input(pesan))
    except ValueError:
        return None


def main():
    tampilkan_menu()
    pilihan = input("Pilihan: ")

    if pilihan == "1":
        p = baca_angka("Panjang: ")
        l = baca_angka("Lebar: ")
        if p is None or l is None:
            print("Masukan harus berupa angka")
        else:
            print("Luas =", luas_persegi_panjang(p, l))
    elif pilihan == "2":
        a = baca_angka("Alas: ")
        t = baca_angka("Tinggi: ")
        if a is None or t is None:
            print("Masukan harus berupa angka")
        else:
            print("Luas =", luas_segitiga(a, t))
    elif pilihan == "3":
        n = baca_bilangan_bulat("n: ")
        if nonnegatif(n):
            print("Jumlah 1 sampai", n, "=", jumlah_n(n))
        else:
            print("n harus bilangan bulat nonnegatif")
    elif pilihan == "4":
        n = baca_bilangan_bulat("n: ")
        if nonnegatif(n):
            print("Faktorial", n, "=", faktorial(n))
        else:
            print("n harus bilangan bulat nonnegatif")
    else:
        print("Pilihan tidak valid")


if __name__ == "__main__":
    main()
