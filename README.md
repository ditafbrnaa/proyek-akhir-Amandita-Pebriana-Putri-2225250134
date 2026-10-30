# Program Rekap dan Analisis Nilai Matematika Kelas

## Deskripsi
Proyek ini dikembangkan untuk menyelesaikan permasalahan rekapitulasi nilai ujian matematika siswa secara otomatis. Program dirancang untuk memproses data nilai mentah dari file teks, melakukan validasi kelayakan nilai (rentang 0 s.d. 100), menghitung statistik kelas secara akurat (rata-rata, nilai minimum, nilai maksimum), menentukan status kelulusan siswa berdasarkan KKM (Kriteria Ketuntasan Minimal), serta menghasilkan laporan terstruktur dalam bentuk file teks. Pengguna sasaran dari program ini adalah guru mata pelajaran atau pengajar les privat dalam mengelola rekap nilai kelas secara efisien.

## Fitur
- Pembacaan data nilai siswa secara otomatis dari file eksternal (`data/nilai_contoh.txt`).
- Validasi data nilai untuk menyaring nilai yang tidak valid atau di luar rentang wajar.
- Perhitungan statistik kelas otomatis (Nilai Rata-rata, Nilai Tertinggi, Nilai Terendah).
- Penentuan status kelulusan siswa secara otomatis berdasarkan KKM (KKM = 70).
- Penyimpanan laporan hasil analisis ke dalam file teks keluaran (`laporan_nilai.txt`).

## Persyaratan
- Python 3.x (disarankan versi 3.10 atau yang lebih baru)
- Modul bawaan Python (Standard Library) tanpa memerlukan instalasi pustaka eksternal tambahan.

## Cara Menjalankan
1. Pastikan struktur folder proyek sudah sesuai (`src/`, `data/`, dll.).
2. Buka terminal di direktori utama proyek.
3. Jalankan perintah berikut untuk mengeksekusi program:
   ```bash
   python src/main.py
   ```

## Struktur Folder
proyek-akhir-Amandita-Pebriana-Putri-2225250134/
│
├── data/
│   └── nilai_contoh.txt          # File data masukan nilai siswa
│
├── src/
│   ├── main.py                   # File utama untuk menjalankan program
│   ├── analisis.py               # Modul logika validasi dan statistik
│   └── data_io.py                # Modul operasi baca/tulis file
│
├── tests/
│   └── test_case.md              # Dokumentasi tabel skenario pengujian
│
├── docs/                         # Dokumen pendukung perancangan
├── .gitignore                    # Berkas pengecualian Git
├── proposal.md                   # Proposal perancangan proyek (Pertemuan 14)
├── laporan_nilai.txt             # Berkas hasil keluaran (output) program
└── README.md                     # Dokumentasi utama proyek

## Test Case
| No | Skenario Uji | Data Masukan (Input) | Harapan Hasil (Expected Output) | Hasil Aktual | Status |
|----|--------------|----------------------|---------------------------------|--------------|--------|
| 1  | Nilai Normal di atas KKM | Nilai: 85, 90 | Status: Lulus, Rata-rata terhitung | Sesuai | PASS |
| 2  | Nilai di bawah KKM (Remedial) | Nilai: 55, 60 | Status: Tidak Lulus / Remidial | Sesuai | PASS |
| 3  | Nilai Tidak Valid (Negatif / >100) | Nilai: -10, 105 | Peringatan diabaikan, data dibuang | Sesuai | PASS |

## Known Issues
- Program saat ini hanya membaca format file teks (.txt) dengan struktur pemisah tertentu; belum mendukung pembacaan langsung dari file lembar kerja berbasis spreadsheet seperti Excel (.xlsx) atau format basis data eksternal.

## Anggota dan Kontribusi
- **Amandita Pebriana Putri (2225250134)**: Perancangan proposal (Pertemuan 14), pengembangan struktur modular kode program (main.py, analisis.py, data_io.py), penyusunan test case, serta dokumentasi README dan penyusunan laporan akhir (Pertemuan 15).

## Referensi/Bantuan
- Modul Bahan Ajar Praktikum Pemrograman Komputer / Proyek Akhir (Pertemuan 14 & 15 - UNTIRTA).
- Dokumentasi resmi bahasa pemrograman Python (docs.python.org) terkait penanganan fungsi dasar berkas dan modularisasi skrip.