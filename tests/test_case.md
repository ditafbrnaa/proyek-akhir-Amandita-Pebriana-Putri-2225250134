from data_io import baca_data, simpan_laporan
from analisis import validasi_nilai, hitung_statistik, tentukan_status

def main():
    print("=== PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA KELAS ===")
    
    # Path file input dan output
    path_input = "../data/nilai_contoh.txt"
    path_output = "../output/laporan_nilai.txt"
    
    # 1. Baca data dari file
    data_mentah = baca_data(path_input)
    if not data_mentah:
        print("Program dihentikan karena tidak ada data yang dapat diproses.")
        return
        
    daftar_nilai_valid = []
    hasil_analisis_siswa = []
    
    # 2. Proses validasi dan analisis per siswa
    for siswa in data_mentah:
        nama = siswa["nama"]
        nilai = siswa["nilai"]
        
        if validasi_nilai(nilai):
            daftar_nilai_valid.append(nilai)
            status = tentukan_status(nilai, kkm=70)
            hasil_analisis_siswa.append({"nama": nama, "nilai": nilai, "status": status})
        else:
            print(f"Peringatan: Nilai {nilai} untuk {nama} diabaikan karena tidak valid.")
            
    # 3. Hitung statistik keseluruhan kelas
    if daftar_nilai_valid:
        rata_rata, nilai_min, nilai_max = hitung_statistik(daftar_nilai_valid)
        
        print("\n--- HASIL ANALISIS STATISTIK KELAS ---")
        print(f"Jumlah Siswa Valid : {len(daftar_nilai_valid)}")
        print(f"Rata-rata Kelas    : {rata_rata:.2f}")
        print(f"Nilai Terendah     : {nilai_min}")
        print(f"Nilai Tertinggi    : {nilai_max}")
        
        # 4. Simpan laporan ke file
        # Pastikan folder output ada atau simpan langsung
        simpan_laporan(path_output, (rata_rata, nilai_min, nilai_max), hasil_analisis_siswa)
    else:
        print("Tidak ada data nilai yang valid untuk dihitung statistiknya.")

if __name__ == "__main__":
    main()