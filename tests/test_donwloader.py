import os
from src.downloader import download_pdfs

def test_download_pdfs():
    pdf_links = ["https://www.example.com/sample.pdf"]
    download_pdfs(pdf_links)

    arquivos = os.listdir("data")
    print("Arquivos na pasta data/:", arquivos)

    assert any(f.endswith(".pdf") for f in arquivos), "Nenhum PDF encontrado na pasta data!"
