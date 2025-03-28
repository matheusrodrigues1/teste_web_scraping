from src.scraper import get_pdf_links
from src.downloader import download_pdfs
from src.compressor import compress_pdfs

def main():
    print("🔍 Buscando links dos PDFs...")
    pdf_links = get_pdf_links()

    print("📥 Baixando PDFs...")
    download_pdfs(pdf_links)

    print("📦 Compactando PDFs...")
    compress_pdfs()

    print("✅ Processo finalizado com sucesso!")

if __name__ == "__main__":
    main()
