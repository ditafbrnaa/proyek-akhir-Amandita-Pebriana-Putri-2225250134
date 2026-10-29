def validasi_nilai(nilai):
    """Memeriksa apakah nilai berada pada rentang valid 0 sampai 100."""
    return 0 <= nilai <= 100

def hitung_statistik(daftar_nilai):
    """Menghitung nilai rata-rata, minimum, dan maksimum dari data nilai."""
    if not daftar_nilai:
        return 0, 0, 0
    
    total = sum(daftar_nilai)
    rata_rata = total / len(daftar_nilai)
    nilai_min = min(daftar_nilai)
    nilai_max = max(daftar_nilai)
    
    return rata_rata, nilai_min, nilai_max

def tentukan_status(nilai, kkm=70):
    """Menentukan status ketuntasan siswa berdasarkan KKM (Kriteria Ketuntasan Minimal)."""
    if nilai >= kkm:
        return "Tuntas"
    else:
        return "Belum Tuntas"