def baca_data(nama_file):
    """Membaca dan memvalidasi data nilai dari file teks baris per baris."""
    data = []
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()
                if not baris:
                    continue  # Lewati baris kosong
                try:
                    parts = baris.split(",")
                    if len(parts) != 2:
                        raise ValueError("Format baris tidak sesuai")
                    nim, teks_nilai = parts
                    nilai = float(teks_nilai)
                    data.append((nim.strip(), nilai))
                except ValueError as e:
                    print(f"Baris {nomor} dilewati karena tidak valid ({e}): {baris}")
    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}. Pastikan path sudah benar.")
    return data

def tulis_rekap(nama_file, data):
    """Menghitung statistik dan menulis ringkasan rekap ke file output."""
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return

    nilai = [item[1] for item in data]
    jumlah_data = len(nilai)
    rata_rata = sum(nilai) / jumlah_data
    nilai_min = min(nilai)
    nilai_max = max(nilai)
    jumlah_lulus = sum(1 for x in nilai if x >= 60)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(f"Jumlah data valid: {jumlah_data}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Minimum: {nilai_min:.2f}\n")
        file.write(f"Maksimum: {nilai_max:.2f}\n")
        file.write(f"Jumlah lulus: {jumlah_lulus}\n")
    print(f"Rekap berhasil ditulis ke {nama_file}")

if __name__ == "__main__":
    input_file = "data/nilai.txt"
    output_file = "data/hasil_rekap.txt"

    print("=== MEMPROSES DATA FILE ===")
    data_valid = baca_data(input_file)
    if data_valid:
        tulis_rekap(output_file, data_valid)