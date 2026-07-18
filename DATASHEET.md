# Datasheet: Wayang-Dataset

Datasheet ini mengikuti kerangka *Datasheets for Datasets* (Gebru et al., 2018) untuk mendokumentasikan motivasi, komposisi, proses pengumpulan, dan keterbatasan dataset secara transparan.

## 1. Motivasi

**Untuk tujuan apa dataset ini dibuat?**
Dataset ini disusun untuk riset klasifikasi karakter wayang kulit purwa gaya Jawa berbasis deep learning, khususnya sebagai data latih dan uji untuk model transfer learning (MobileNetV3-Small dan EfficientNet-B0) dengan analisis Explainable AI (Grad-CAM, feature ablation).

**Siapa yang membuat dataset ini dan atas nama siapa?**
Disusun oleh mahasiswa Departemen Informatika, Universitas Muhammadiyah Malang, sebagai bagian dari tugas akhir (Laporan Akhir).

**Siapa yang mendanai pembuatan dataset ini?**
Tidak ada pendanaan eksternal; dikumpulkan secara mandiri oleh penyusun.

## 2. Komposisi

**Apa yang direpresentasikan oleh instance dalam dataset ini?**
Setiap instance adalah satu citra digital yang menampilkan wujud wayang kulit purwa dari satu tokoh tertentu.

**Berapa banyak instance yang ada, per kelas?**

| No | Kelas | Kelompok | Jumlah Citra |
|----|-------|----------|--------------|
| 1 | Arjuna | Pandawa Lima | 120 |
| 2 | Bagong | Punakawan | 121 |
| 3 | Bima | Pandawa Lima | 122 |
| 4 | Gareng | Punakawan | 114 |
| 5 | NakulaSadewa | Pandawa Lima | 122 |
| 6 | Petruk | Punakawan | 128 |
| 7 | Semar | Punakawan | 120 |
| 8 | Yudhistira | Pandawa Lima | 120 |
| | **Total** | | **967** |

**Catatan komposisi khusus:**
Kelas **NakulaSadewa** menggabungkan dua tokoh kembar (Nakula dan Sadewa) menjadi satu kelas karena kemiripan visual yang sangat tinggi antar keduanya, untuk mencegah ambiguitas label dan potensi duplikasi anotasi antar kelas yang sebenarnya sulit dibedakan bahkan secara visual oleh manusia.

**Apakah dataset ini memuat seluruh populasi yang mungkin, atau sampel?**
Sampel. Populasi wayang kulit purwa gaya Jawa (khususnya gaya Surakarta/Yogyakarta) memiliki variasi bentuk yang sangat banyak antar dalang/sanggar; dataset ini tidak mengklaim mencakup seluruh variasi gaya yang ada.

**Format data apa yang tersedia untuk tiap instance?**
Citra digital format JPG/PNG, resolusi bervariasi (tidak diseragamkan pada tahap pengumpulan mentah).

**Apakah ada label atau target terkait tiap instance?**
Ya — nama kelas karakter (8 kelas, lihat tabel di atas), direpresentasikan melalui struktur folder (`data/{split}/{class_name}/`).

**Apakah ada informasi yang hilang dari masing-masing instance?**
Ya — sebagian besar instance tidak memiliki catatan URL sumber individual (lihat bagian Proses Pengumpulan).

## 3. Proses Pengumpulan

**Bagaimana data pada tiap instance diperoleh?**
Kombinasi tiga metode:
- **Scraping** — pengambilan otomatis dari hasil pencarian gambar
- **Unduhan manual** — diunduh langsung oleh penyusun dari platform tertentu
- **Tangkapan layar (screenshot)** — diambil dari tampilan platform, termasuk halaman produk e-commerce

**Dari platform mana data dikumpulkan?**
Pinterest, Google Images, Instagram, Shopee, Tokopedia, serta kompilasi daring [*Album Wayang Indonesia*](https://tokohwayangpurwa.blogspot.com/) — sebuah situs agregator non-komersial. Berdasarkan pernyataan situs tersebut, citra pada blog ini berasal dari kombinasi koleksi pribadi penyusun blog, sanggar wayang, kontributor komunitas (termasuk berbagai akun Facebook pelaku/kolektor wayang), dan publikasi cetak — bukan karya tunggal satu pihak.

**Kapan data dikumpulkan?**
Periode pengumpulan bertahap selama proses penyusunan tugas akhir; tanggal pasti per-citra tidak seluruhnya tercatat.

**Keterbatasan Provenance (penting):**
URL sumber individual untuk sebagian besar citra **tidak tercatat** pada saat pengumpulan, karena pencatatan sistematis belum diterapkan di tahap awal proyek. Informasi sumber yang tersedia di `annotations/provenance.csv` bersifat **platform-level** (berdasarkan ingatan penyusun), bukan tautan langsung yang terverifikasi per-gambar. Pengguna yang membutuhkan verifikasi sumber individual dapat melakukan reverse image search (Google Lens, TinEye).

## 4. Proses Anotasi (Pelabelan)

**Siapa yang melakukan anotasi/pelabelan?**
Dilakukan oleh satu orang (penyusun dataset) tanpa anotator kedua. Ini merupakan keterbatasan yang diakui — tidak ada pengukuran *inter-annotator agreement* formal.

**Bagaimana proses pelabelan dilakukan?**
Pelabelan dilakukan berdasarkan identifikasi visual atribut karakteristik tiap tokoh wayang (bentuk wajah, mahkota/gelung, warna, aksesori/pusaka) dengan rujukan pada sumber referensi ikonografi wayang purwa gaya Surakarta/Yogyakarta. Lihat `docs/annotation_guidelines.md` untuk kriteria detail per kelas.

**Bagaimana kasus ambigu ditangani?**
Kasus paling signifikan adalah kemiripan visual Nakula–Sadewa, ditangani dengan penggabungan kelas (lihat bagian Komposisi).

## 5. Preprocessing/Pembersihan

**Preprocessing apa yang telah dilakukan pada data mentah?**
Normalisasi format citra dilakukan menggunakan skrip Python berbasis Pillow, menyesuaikan struktur folder Train/Val/Test. Resize/augmentasi lanjutan diserahkan kepada pengguna sesuai kebutuhan arsitektur model masing-masing (tidak diterapkan permanen pada file yang didistribusikan).

**Apakah data mentah (sebelum preprocessing) juga disimpan?**
Tidak didistribusikan terpisah; yang tersedia adalah versi setelah normalisasi format.

## 6. Penggunaan

**Untuk tugas apa dataset ini telah digunakan?**
Klasifikasi citra 8 kelas menggunakan transfer learning (MobileNetV3-Small, EfficientNet-B0) dengan analisis XAI (Grad-CAM, feature ablation).

**Apakah ada risiko atau keterbatasan yang perlu diperhatikan pengguna lain?**
- Distribusi kelas tidak sepenuhnya seimbang (114–128 citra per kelas).
- Campuran citra dokumentasi budaya (variatif: pencahayaan, sudut, latar) dan citra produk e-commerce (umumnya latar polos studio) berpotensi memengaruhi generalisasi model terhadap kondisi dunia nyata.
- Provenance citra individual tidak seluruhnya dapat diverifikasi.
- Anotasi dilakukan oleh satu orang tanpa validasi silang formal.

## 7. Distribusi

**Bagaimana dataset ini didistribusikan?**
Melalui GitHub (struktur folder + kode) dan GitHub Releases (arsip ZIP), serta dicerminkan (mirror) di Kaggle.

**Di bawah lisensi apa dataset ini didistribusikan?**
- Kode & anotasi: MIT License
- Data citra: CC BY-NC 4.0 (lihat `DATA_LICENSE`) — dengan catatan status hak cipta citra individual bervariasi menurut sumber dan tidak seluruhnya terverifikasi; digunakan di bawah klaim *fair use* akademik untuk riset non-komersial.

## 8. Pemeliharaan

**Siapa yang memelihara dataset ini?**
Penyusun dataset (kontak: orangeformepoof@gmail.com).

**Bagaimana mekanisme takedown/permintaan penghapusan?**
Pemilik hak cipta yang berkeberatan atas penggunaan citra tertentu dapat menghubungi kontak di atas untuk permintaan penghapusan; permintaan akan ditindaklanjuti pada rilis versi berikutnya.
