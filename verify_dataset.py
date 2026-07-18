"""
verify_dataset.py

Skrip verifikasi integritas Wayang-Dataset.
Menghitung checksum SHA256 seluruh file citra di folder data/,
lalu membandingkannya dengan file referensi checksums.csv (jika tersedia).

Cara pakai:
    # Membuat file referensi checksum (dijalankan sekali oleh penyusun dataset)
    python verify_dataset.py --generate

    # Memverifikasi dataset yang sudah diunduh oleh pengguna lain
    python verify_dataset.py --verify
"""

import argparse
import csv
import hashlib
import sys
from pathlib import Path

DATA_DIR = Path("data")
CHECKSUM_FILE = Path("annotations/checksums.csv")
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}


def compute_sha256(filepath: Path) -> str:
    """Menghitung hash SHA256 dari sebuah file secara streaming (hemat memori)."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def collect_image_files(root: Path):
    """Mengumpulkan semua file citra di bawah root, terurut agar hasil konsisten."""
    files = [
        p for p in root.rglob("*")
        if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS
    ]
    return sorted(files)


def generate_checksums():
    if not DATA_DIR.exists():
        print(f"Error: folder '{DATA_DIR}' tidak ditemukan.")
        sys.exit(1)

    files = collect_image_files(DATA_DIR)
    if not files:
        print(f"Peringatan: tidak ada file citra ditemukan di '{DATA_DIR}'.")
        sys.exit(1)

    CHECKSUM_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CHECKSUM_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["relative_path", "sha256"])
        for filepath in files:
            rel_path = filepath.relative_to(Path(".")).as_posix()
            checksum = compute_sha256(filepath)
            writer.writerow([rel_path, checksum])
            print(f"  {rel_path}: {checksum}")

    print(f"\nSelesai. {len(files)} checksum disimpan ke '{CHECKSUM_FILE}'.")


def verify_checksums():
    if not CHECKSUM_FILE.exists():
        print(f"Error: file referensi '{CHECKSUM_FILE}' tidak ditemukan.")
        print("Jalankan dengan --generate terlebih dahulu jika Anda penyusun dataset.")
        sys.exit(1)

    reference = {}
    with open(CHECKSUM_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            reference[row["relative_path"]] = row["sha256"]

    mismatches = []
    missing = []

    for rel_path, expected_hash in reference.items():
        filepath = Path(rel_path)
        if not filepath.exists():
            missing.append(rel_path)
            continue
        actual_hash = compute_sha256(filepath)
        if actual_hash != expected_hash:
            mismatches.append(rel_path)

    print(f"Total file dicek : {len(reference)}")
    print(f"File hilang      : {len(missing)}")
    print(f"File tidak cocok : {len(mismatches)}")

    if missing:
        print("\nFile yang hilang:")
        for m in missing:
            print(f"  - {m}")

    if mismatches:
        print("\nFile dengan checksum tidak cocok (kemungkinan rusak/berubah):")
        for m in mismatches:
            print(f"  - {m}")

    if not missing and not mismatches:
        print("\n✅ Semua file terverifikasi cocok dengan referensi.")
    else:
        print("\n⚠️ Ditemukan ketidaksesuaian. Pertimbangkan mengunduh ulang dataset.")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Verifikasi integritas Wayang-Dataset.")
    parser.add_argument(
        "--generate", action="store_true",
        help="Buat file referensi checksum baru dari data/ (untuk penyusun dataset)."
    )
    parser.add_argument(
        "--verify", action="store_true",
        help="Verifikasi data/ terhadap file referensi checksum (untuk pengguna dataset)."
    )
    args = parser.parse_args()

    if args.generate:
        generate_checksums()
    elif args.verify:
        verify_checksums()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
