# Pertemuan 07 Fungsi Python

Nama: Rasyad Fazri Mulyono
NIM: 2225250023
Kelas: 3A

Mata kuliah Algoritma dan Pemrograman, Program Studi Pendidikan Matematika FKIP Universitas Sultan Ageng Tirtayasa.

## Tujuan

Menggunakan fungsi, parameter, return value, dan scope untuk membuat program modular.

## Cara Menjalankan

Jalankan dari folder utama repositori. Pada Windows, gunakan `python` sebagai pengganti `python3`.

Praktik 2 (program berbasis menu):

```
python3 praktik/utilitas_matematika.py
```

Latihan 1 sampai 5:

```
python3 latihan/01_salam.py
python3 latihan/02_luas_persegi_panjang.py
python3 latihan/03_jumlah_n.py
python3 latihan/04_statistik_sederhana.py
python3 latihan/05_scope.py
```

## Struktur Folder

```
pertemuan-07-fungsi-2225250023/
|-- README.md
|-- .gitignore
|-- latihan/
|   |-- 01_salam.py
|   |-- 02_luas_persegi_panjang.py
|   |-- 03_jumlah_n.py
|   |-- 04_statistik_sederhana.py
|   `-- 05_scope.py
`-- praktik/
    `-- utilitas_matematika.py
```

## Struktur Fungsi

### Praktik 2: `praktik/utilitas_matematika.py`

| Fungsi | Parameter | Nilai return | Keterangan |
|---|---|---|---|
| `luas_persegi_panjang(p, l)` | `p` panjang, `l` lebar | `p * l` | Menghitung luas persegi panjang |
| `luas_segitiga(a, t)` | `a` alas, `t` tinggi | `0.5 * a * t` | Menghitung luas segitiga |
| `jumlah_n(n)` | `n` bilangan bulat nonnegatif | Jumlah 1 + 2 + ... + n | Memakai perulangan `for` |
| `faktorial(n)` | `n` bilangan bulat nonnegatif | n! | Memakai perulangan `for` |
| `nonnegatif(n)` | `n` nilai yang diperiksa | `True` atau `False` | Memeriksa n bilangan bulat nonnegatif |
| `tampilkan_menu()` | tidak ada | tidak ada | Hanya menampilkan pilihan operasi |
| `baca_angka(pesan)` | `pesan` teks permintaan masukan | `float` atau `None` | `None` jika masukan bukan angka |
| `baca_bilangan_bulat(pesan)` | `pesan` teks permintaan masukan | `int` atau `None` | `None` jika masukan bukan bilangan bulat |
| `main()` | tidak ada | tidak ada | Program utama, memakai seleksi untuk memanggil fungsi sesuai pilihan |

Perhitungan berada di fungsi dan dikembalikan dengan `return`. Interaksi dengan pengguna (`input` dan `print`) berada di `main()`.

### Latihan: `latihan/`

| Berkas | Fungsi | Parameter | Nilai return |
|---|---|---|---|
| `01_salam.py` | `salam(nama)` | `nama` | tidak ada (mencetak salam) |
| `01_salam.py` | `salam_kelas(nama, kelas)` | `nama`, `kelas` | tidak ada (mencetak nama dan kelas) |
| `02_luas_persegi_panjang.py` | `luas_persegi_panjang(p, l)` | `p`, `l` | luas |
| `03_jumlah_n.py` | `jumlah_n(n)` | `n` | jumlah 1 sampai n |
| `03_jumlah_n.py` | `jumlah_rumus(n)` | `n` | n(n+1)/2 |
| `04_statistik_sederhana.py` | `statistik(data)` | `data` (list) | tuple (minimum, maksimum, rata-rata) |
| `05_scope.py` | `demo(x)` | `x` | `x + 5` |

## Hasil Pengujian

### Praktik 2 (test case wajib)

| Operasi | Input | Hasil yang diharapkan | Hasil aktual | Status |
|---|---|---|---|---|
| Luas persegi panjang | p=8, l=5 | 40 | 40.0 | Lulus |
| Luas segitiga | a=10, t=6 | 30.0 | 30.0 | Lulus |
| Jumlah 1..n | n=10 | 55 | 55 | Lulus |
| Faktorial | n=5 | 120 | 120 | Lulus |
| Faktorial | n=0 | 1 | 1 | Lulus |

Pengujian validasi dan kasus khusus:

| Kasus | Input | Hasil yang diharapkan | Hasil aktual | Status |
|---|---|---|---|---|
| Faktorial dengan n negatif | n=-3 | Pesan "n harus bilangan bulat nonnegatif" | Sesuai | Lulus |
| Jumlah dengan n desimal | n=2.5 | Pesan "n harus bilangan bulat nonnegatif" | Sesuai | Lulus |
| Faktorial dengan n bukan angka | n=abc | Pesan "n harus bilangan bulat nonnegatif" | Sesuai | Lulus |
| Luas dengan panjang bukan angka | p=x | Pesan "Masukan harus berupa angka" | Sesuai | Lulus |
| Pilihan menu di luar 1-4 | 9 | Pesan "Pilihan tidak valid" | Sesuai | Lulus |

### Latihan

| Latihan | Input | Hasil yang diharapkan | Hasil aktual | Status |
|---|---|---|---|---|
| 2 | (8, 5) | 40 | 40 | Lulus |
| 2 | (2.5, 4) | 10 | 10.0 | Lulus |
| 2 | (0, 7) | 0 | 0 | Lulus |
| 3 | n=1 | 1 | 1 | Lulus |
| 3 | n=5 | 15 | 15 | Lulus |
| 3 | n=10 | 55 | 55 | Lulus |
| 3 | n=100 | 5050 | 5050 | Lulus |
| 4 | [70, 80, 65, 90, 75] | (65, 90, 76.0) | (65, 90, 76.0) | Lulus |
| 5 | demo(20), x global = 10 | di dalam: 20 25, di luar: 10 25 | di dalam: 20 25, di luar: 10 25 | Lulus |

Pada Latihan 3, hasil perulangan sama dengan hasil rumus n(n+1)/2 untuk semua nilai n yang diuji.

## Refleksi

Bagian yang menjadi lebih sederhana setelah dipisah menjadi fungsi adalah program utama pada Praktik 2. Rumus luas, penjumlahan, dan faktorial cukup ditulis satu kali di fungsinya masing-masing, sehingga program utama hanya memilih fungsi mana yang dipanggil. Karena setiap fungsi punya input dan output yang jelas, saya bisa menguji tiap fungsi sendiri dengan test case, dan kesalahan lebih mudah dicari.

## Sumber dan Bantuan

- Bahan ajar Pertemuan 7 Algoritma dan Pemrograman (Dr. Aan Hendrayana, S.Si., M.Pd.).
- Dokumentasi Python 3: Defining Functions.
- Kode latihan dan Praktik 2 disusun dengan bantuan Claude, kemudian dijalankan dan diuji. Saya mempelajari dan dapat menjelaskan kode tersebut.
