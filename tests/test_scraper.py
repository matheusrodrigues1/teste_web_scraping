from src.scraper import get_pdf_links

def test_get_pdf_links():
    pdf_links = get_pdf_links()
    assert isinstance(pdf_links, list)
    assert all(link.endswith(".pdf") for link in pdf_links)
