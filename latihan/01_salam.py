# Latihan 1: Fungsi Salam

def salam(nama):
    print(f"Halo, {nama}. Selamat belajar Python!")


# Modifikasi: fungsi menerima parameter kelas dan menampilkan nama serta kelas
def salam_kelas(nama, kelas):
    print(f"Halo, {nama} dari kelas {kelas}. Selamat belajar Python!")


print("--- Versi awal ---")
salam("Alya")
salam("Bima")

print("--- Versi modifikasi (nama dan kelas) ---")
salam_kelas("Alya", "3A")
salam_kelas("Bima", "3B")
