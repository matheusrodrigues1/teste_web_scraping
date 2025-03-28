import requests
from bs4 import BeautifulSoup

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

def get_pdf_links():
    """Extrai os links dos PDFs da página"""
    response = requests.get(URL)
    if response.status_code != 200:
        raise Exception("Erro ao acessar o site!")

    soup = BeautifulSoup(response.text, 'html.parser')
    pdf_links = [
        link["href"] for link in soup.find_all("a", href=True)
        if link["href"].endswith(".pdf") and ("Anexo-I" in link["href"] or "Anexo-II" in link["href"])
    ]

    return pdf_links
