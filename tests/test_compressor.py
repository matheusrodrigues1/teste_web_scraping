import os
from src.compressor import compress_pdfs

def test_compress_pdfs():
    compress_pdfs()
    assert os.path.exists("output/anexos.zip")
