# Wayang-Dataset

Dataset citra wayang kulit purwa untuk tugas klasifikasi karakter berbasis deep learning (Pandawa Lima & Punakawan), disusun sebagai bagian dari riset skripsi Departemen Informatika, Universitas Muhammadiyah Malang.

## Sumber Data

Dataset ini dikumpulkan melalui kombinasi scraping, unduhan manual, dan tangkapan layar dari beberapa platform publik: Pinterest, Google Images, Instagram, Shopee, Tokopedia, serta kompilasi daring [*Album Wayang Indonesia*](https://tokohwayangpurwa.blogspot.com/).

⚠️ **Keterbatasan**: URL sumber per-gambar tidak seluruhnya tercatat karena pengumpulan dilakukan pada tahap awal proyek tanpa pencatatan sistematis. Informasi sumber tersedia pada level platform, bukan per-citra. Detail lengkap ada di [`DATASHEET.md`](./DATASHEET.md).

Dataset ini disediakan untuk **tujuan riset dan pendidikan non-komersial**. Jika Anda adalah pemilik hak cipta salah satu citra dan keberatan dengan penggunaannya, silakan hubungi **orangeformepoof@gmail.com** untuk permintaan penghapusan.

## Karakter Wayang

Dataset ini meliputi dua kelompok, yaitu Pandawa Lima dan Punakawan.

- **Pandawa Lima**: Arjuna, Bima, NakulaSadewa, Yudhistira.
  Kelas **NakulaSadewa** merupakan tokoh kembar dengan kemiripan visual yang tinggi, sehingga pada dataset ini digabung menjadi satu kelas untuk mencegah ambiguitas anotasi/duplikasi label.
- **Punakawan**: Bagong, Gareng, Petruk, Semar.

| No | Kelas | Jumlah Citra |
|----|-------|--------------|
| 1 | Arjuna | 120 |
| 2 | Bagong | 121 |
| 3 | Bima | 122 |
| 4 | Gareng | 114 |
| 5 | NakulaSadewa | 122 |
| 6 | Petruk | 128 |
| 7 | Semar | 120 |
| 8 | Yudhistira | 120 |
| | **Total** | **967** |

## Karakteristik Dataset

Dataset ini meliputi kondisi yang bervariasi dari segi pencahayaan, resolusi, sudut pengambilan gambar, kontras, warna, dan latar belakang — termasuk variasi antara citra dokumentasi pertunjukan/koleksi budaya dan citra foto produk (mis. dari Shopee/Tokopedia) yang cenderung berlatar polos studio.

## Struktur Dataset

```
Wayang-Dataset/
├── README.md
├── DATASHEET.md
├── LICENSE
├── DATA_LICENSE
├── CITATION.cff
├── data/
│   ├── train/
│   │   ├── Arjuna/
│   │   ├── Bagong/
│   │   ├── Bima/
│   │   ├── Gareng/
│   │   ├── NakulaSadewa/
│   │   ├── Petruk/
│   │   ├── Semar/
│   │   └── Yudhistira/
│   ├── val/
│   │   └── ... (struktur kelas sama seperti train)
│   └── test/
│       └── ... (struktur kelas sama seperti train)
├── annotations/
│   └── provenance.csv
├── scripts/
│   └── verify_dataset.py
└── docs/
    └── annotation_guidelines.md
```

## Pembagian Data (Split)

<!-- TODO: isi rasio split aktual, mis. 70% train / 15% val / 15% test -->
Rasio pembagian train/val/test: **[isi di sini, mis. 80/10/10]**. Pembagian dilakukan secara stratified per kelas untuk menjaga proporsi antar kelas tetap konsisten di setiap subset.

## Lisensi

- **Anotasi & kode** (skrip preprocessing, label, dokumentasi): [MIT License](./LICENSE)
- **Data citra**: [CC BY-NC 4.0](./DATA_LICENSE) — status hak cipta citra individual bervariasi menurut platform sumber dan tidak seluruhnya terverifikasi (lihat `DATASHEET.md`). Citra digunakan di bawah klaim *fair use* akademik untuk riset non-komersial.

## Cara Penggunaan

```python
import os
from pathlib import Path

data_dir = Path("data/train")
classes = sorted(os.listdir(data_dir))
print(classes)
# ['Arjuna', 'Bagong', 'Bima', 'Gareng', 'NakulaSadewa', 'Petruk', 'Semar', 'Yudhistira']
```

Verifikasi integritas file setelah mengunduh:
```bash
python scripts/verify_dataset.py
```

## Sitasi

Jika Anda menggunakan dataset ini dalam riset, mohon sitasi sesuai `CITATION.cff`, atau:

```
[Fathimatuz Z.]. (2026). Wayang-Dataset: Wayang Kulit Purwa Character Classification Dataset (v1.0.0) [Data set].
GitHub. https://github.com/[amocca]/Wayang-Dataset
```

## Kontak

Pertanyaan, laporan kesalahan anotasi, atau permintaan penghapusan citra: **orangeformepoof@gmail.com**
