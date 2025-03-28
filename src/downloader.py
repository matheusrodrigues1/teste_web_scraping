import os
import requests

DATA_DIR = "data"

def download_pdfs(pdf_links):
    """Baixa os PDFs encontrados na página"""
    os.makedirs(DATA_DIR, exist_ok=True)

    for link in pdf_links:
        file_name = os.path.join(DATA_DIR, link.split("/")[-1])
        
        response = requests.get(link, stream=True)
        if response.status_code == 200:
            with open(file_name, "wb") as file:
                file.write(response.content)
            print(f"Baixado: {file_name}")
        else:
            print(f"Erro ao baixar {link}")

if __name__ == "__main__":
    from scraper import get_pdf_links
    pdf_links = get_pdf_links()
    download_pdfs(pdf_links)
