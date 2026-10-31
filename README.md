# Pertemuan 12 File I/O dan Error Handling

Nama: Sheila Ni'matul Hasanah
NIM: 2225250138
Kelas: 3B

## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file dengan Python.

## Format File Input
NIM, nilai.

## Cara Menjalankan
```bash
python3 tugas/rekap_nilai_file.py
```

## Error yang Ditangani
* **`FileNotFoundError`**: Ditangani ketika file input (`data/nilai.txt`) tidak ditemukan di direktori, sehingga program menampilkan pesan peringatan dan tidak *crash*.
* **`ValueError`**: Ditangani ketika baris data memiliki format nilai yang tidak valid (misalnya berupa teks alih-alih angka), sehingga baris tersebut dilewati dan diproses dengan aman tanpa menghentikan keseluruhan program.

## Test Case
| Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- |
| Normal (Semua baris valid) | Semua record diproses dan rekap benar | Semua record diproses dan rekap benar | Lulus |
| File hilang (`nilai.txt` tidak ada) | Pesan file tidak ditemukan; program tidak *crash* | Pesan file tidak ditemukan; program tidak *crash* | Lulus |
| Nilai invalid (`A004,abc`) | Baris invalid dilewati/dilaporkan; record lain tetap diproses | Baris invalid dilewati/dilaporkan; record lain tetap diproses | Lulus |
| Baris kosong | Baris kosong dilewati | Baris kosong dilewati | Lulus |
| Batas lulus (Nilai 60) | Dihitung sebagai lulus | Dihitung sebagai lulus | Lulus |

## Refleksi
Kesalahan error yang sempat diantisipasi adalah mencegah program berhenti secara tiba-tiba (*crash*) ketika menemui baris data dengan format nilai teks yang tidak valid (`ValueError`) atau file yang belum tersedia (`FileNotFoundError`), sehingga proses rekapitulasi statistik nilai valid tetap berjalan dengan akurat.
