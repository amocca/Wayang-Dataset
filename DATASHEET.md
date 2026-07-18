## Collection Process — Sumber dan Provenance

### Metode Pengumpulan
| Metode | Deskripsi |
|---|---|
| Scraping | Otomatis dari hasil pencarian gambar |
| Unduhan manual | Diunduh langsung oleh penyusun dataset |
| Tangkapan layar | Diambil dari tampilan platform (mis. video, katalog produk) |

### Platform Sumber
- **Pinterest** — repost/kurasi, atribusi ke pembuat asli sering tidak tersedia di platform
- **Google Images** — hasil pencarian gambar, sumber asli bervariasi
- **Instagram** — repost/kurasi, atribusi ke pembuat asli sering tidak tersedia di platform
- **Shopee & Tokopedia** — foto produk kerajinan/souvenir wayang kulit, bukan foto pertunjukan
- **Album Wayang Indonesia** (tokohwayangpurwa.blogspot.com) — situs agregator non-komersial; menurut pernyataan situs tersebut, gambar berasal dari kombinasi koleksi pribadi penyusun blog, sanggar wayang, kontributor komunitas, dan publikasi cetak (bukan karya tunggal satu pihak)

### Keterbatasan Provenance
URL sumber individual untuk sebagian besar citra **tidak tercatat** pada saat pengumpulan. Metadata yang tersedia (`provenance.csv`) mencantumkan platform asal per-citra berdasarkan ingatan penyusun, bukan tautan langsung terverifikasi. Pengguna yang membutuhkan verifikasi sumber dapat melakukan reverse image search (Google Lens/TinEye).

### Implikasi Metodologis
Citra dari Shopee/Tokopedia umumnya berupa foto produk (latar polos, pencahayaan studio), berbeda karakteristiknya dari citra hasil pertunjukan/dokumentasi budaya (Pinterest, Instagram, blog). Percampuran ini berpotensi memengaruhi variasi visual dalam dataset dan digambarkan pada bagian analisis keterbatasan (§4.3) laporan terkait.
