import os
import shutil

DATA_DIR = "data"
OUTPUT_DIR = "output"
ZIP_FILE = os.path.join(OUTPUT_DIR, "anexos.zip")

def compress_pdfs():
    """Compacta os PDFs baixados em um arquivo ZIP"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    shutil.make_archive(ZIP_FILE.replace(".zip", ""), 'zip', DATA_DIR)
    print(f"Compactado em: {ZIP_FILE}")

if __name__ == "__main__":
    compress_pdfs()
