# Panduan Anotasi — Wayang-Dataset

Dokumen ini menjelaskan kriteria visual yang digunakan untuk melabeli tiap citra ke dalam 8 kelas karakter wayang kulit purwa, serta bagaimana kasus ambigu ditangani.

## Prinsip Umum

- Anotasi dilakukan oleh satu orang (penyusun dataset), berdasarkan identifikasi atribut visual karakteristik tiap tokoh: bentuk wajah, mahkota/gelung, warna kulit wayang, dan aksesori/pusaka khas.
- Rujukan utama: ikonografi wayang purwa gaya Surakarta dan Yogyakarta.
- Citra yang tidak dapat diidentifikasi dengan yakin (buram, terpotong, atau tokoh tidak dikenali) **tidak dimasukkan** ke dalam dataset.

## Kriteria per Kelas

### Pandawa Lima

| Kelas | Ciri Visual Utama |
|---|---|
| **Arjuna** | Wajah halus (luruh), tubuh langsing, mahkota sederhana tanpa jamang besar; sering digambarkan dengan busur panah (Gandiwa) sebagai atribut. |
| **Bima** | Tubuh besar dan tegap, kuku panjang (Pancanaka) di ibu jari, memakai gelang/kalung besar, posisi kaki khas (kuda-kuda lebar), warna kulit hitam. |
| **NakulaSadewa** | Wajah kembar identik, tubuh proporsional sedang, mahkota mirip satu sama lain. **Digabung menjadi satu kelas** karena tingkat kemiripan visual antara Nakula dan Sadewa sangat tinggi, sehingga pemisahan berisiko menghasilkan label yang tidak konsisten/ambigu. |
| **Yudhistira** | Wajah tenang (luruh), postur sederhana, mahkota minimal/tanpa hiasan berlebih, mencerminkan karakter bijaksana. |

### Punakawan

| Kelas | Ciri Visual Utama |
|---|---|
| **Semar** | Tubuh bulat/gemuk, wajah khas dengan mata sipit dan mulut tersenyum, tidak memakai mahkota, warna kulit kombinasi hitam-putih. |
| **Gareng** | Tubuh pendek, mata juling, tangan patah/tidak simetris, kaki pincang — ciri fisik yang menonjol dan mudah dibedakan dari Punakawan lain. |
| **Petruk** | Tubuh tinggi kurus, hidung panjang mencolok, tangan panjang. |
| **Bagong** | Tubuh bulat pendek, wajah lebar dengan mulut besar, mirip siluet Semar namun lebih pendek dan tanpa detail wajah setua Semar. |

## Penanganan Kasus Ambigu

1. **Nakula vs Sadewa** — digabung menjadi kelas `NakulaSadewa` (lihat tabel di atas). Ini adalah keputusan desain yang disengaja, bukan kesalahan anotasi.
2. **Variasi gaya regional (Surakarta vs Yogyakarta vs Bali)** — kedua gaya utama (Surakarta/Yogyakarta) tetap dimasukkan dalam kelas yang sama selama identitas tokoh dapat dikenali, karena penelitian ini berfokus pada klasifikasi tokoh, bukan klasifikasi gaya regional.
3. **Citra dengan atribut pusaka yang tertutup/tidak terlihat** — tetap dapat dilabeli selama ciri wajah dan tubuh cukup jelas untuk identifikasi.
4. **Citra buram, resolusi sangat rendah, atau sudut ekstrem yang menyulitkan identifikasi** — dikeluarkan dari dataset, tidak dipaksakan masuk kelas manapun.

## Keterbatasan Proses Anotasi

Karena anotasi dilakukan oleh satu orang tanpa anotator kedua, tidak ada pengukuran *inter-annotator agreement* (mis. Cohen's Kappa) yang dapat dilaporkan. Sebagai gantinya, disarankan bagi pengguna dataset yang membutuhkan jaminan kualitas label lebih tinggi untuk melakukan audit sampel acak terhadap subset kecil dataset ini secara independen.
