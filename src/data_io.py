import os

def baca_data(path_file):
    """Membaca data siswa dan nilai dari file teks eksternal."""
    data_siswa = []
    try:
        if not os.path.exists(path_file):
            print(f"Peringatan: File {path_file} tidak ditemukan.")
            return data_siswa
            
        with open(path_file, 'r', encoding='utf-8') as file:
            for baris in file:
                baris = baris.strip()
                if baris:
                    parts = baris.split(',')
                    if len(parts) == 2:
                        nama = parts[0].strip()
                        try:
                            nilai = float(parts[1].strip())
                            data_siswa.append({"nama": nama, "nilai": nilai})
                        except ValueError:
                            print(f"Peringatan: Nilai tidak valid untuk {nama}")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")
        
    return data_siswa

def simpan_laporan(path_output, statistik, hasil_siswa):
    """Menyimpan hasil rekapitulasi analisis nilai ke dalam file laporan teks."""
    try:
        with open(path_output, 'w', encoding='utf-8') as file:
            file.write("=== LAPORAN REKAPITULASI NILAI MATEMATIKA KELAS ===\n\n")
            file.write(f"Rata-rata Kelas : {statistik[0]:.2f}\n")
            file.write(f"Nilai Terendah  : {statistik[1]}\n")
            file.write(f"Nilai Tertinggi : {statistik[2]}\n\n")
            file.write("--- DETAIL STATUS SISWA ---\n")
            for item in hasil_siswa:
                file.write(f"Nama: {item['nama']} | Nilai: {item['nilai']} | Status: {item['status']}\n")
        print(f"Laporan berhasil disimpan ke {path_output}")
    except Exception as e:
        print(f"Gagal menyimpan laporan: {e}")