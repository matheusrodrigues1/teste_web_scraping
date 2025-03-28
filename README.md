# Teste Web Scraping

Este projeto realiza web scraping para extrair links de arquivos PDF de uma página da web, baixa os PDFs, e os compacta em um arquivo `.zip`. O objetivo é automatizar o processo de extração e organização de arquivos de uma página da web para facilitar o armazenamento e a manipulação posterior.

## Estrutura do Projeto

teste_web_scraping/</br>
│── main.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Arquivo principal para rodar o processo completo</br>
│── requirements.txt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Lista de dependências do projeto</br>
│── README.md&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Explicação sobre o projeto e como executar</br>
│── src/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Código-fonte do projeto</br>
│ │── **init**.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Arquivo para definir o diretório como módulo Python</br>
│ │── scraper.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Módulo para extrair os links dos PDFs</br>
│ │── downloader.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Módulo para baixar os PDFs</br>
│ │── compressor.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Módulo para compactar os arquivos</br>
│── data/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Diretório onde os PDFs baixados serão armazenados</br>
│── output/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Diretório onde o arquivo compactado será salvo</br>
│── tests/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Diretório para testes automatizados</br>
│ │── test_scraper.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Testes para scraper.py</br>
│ │── test_downloader.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Testes para downloader.py</br>
│ │── test_compressor.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Testes para compressor.py</br>

## Como Executar

1. **Clone o repositório**:

   Clone este repositório para sua máquina local:

   ```bash
   git clone https://github.com/matheusrodrigues1/teste_web_scraping
   cd web_scraping_project
   ```

2. Configuração do Ambiente Virtual (venv):

   ```bash
     python -m venv venv
     source venv/bin/activate  # No Linux/Mac
     # ou
     venv\Scripts\activate     # No Windows

   ```

3. **Instale as dependências**:

   O projeto depende de várias bibliotecas Python. Instale-as usando o pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o script principal**:

   Para rodar o processo completo de scraping, download e compressão, execute o arquivo main.py:

   ```bash
   python main.py
   ```

   O script irá:

   - Realizar o scraping da página para extrair os links dos arquivos PDF.

   - Baixar os PDFs encontrados.

   - Compactar os PDFs em um arquivo .zip que será salvo no diretório output/.

5. **Diretórios**:

   - Os PDFs baixados serão armazenados no diretório data/.

   - O arquivo .zip contendo os PDFs compactados será salvo no diretório output/.

## Estrutura dos Módulos

- scraper.py: Este módulo é responsável por acessar a página da web e extrair os links dos arquivos PDF.

- downloader.py: Módulo para baixar os PDFs usando os links extraídos pelo scraper.

- compressor.py: Módulo para compactar os PDFs baixados em um arquivo .zip.

## Teste

O projeto inclui testes automatizados para garantir que os módulos funcionem corretamente.

Para rodar os testes, use o framework de testes do Python, pytest:

```bash
pytest tests/
```

Desde já obrigado pela oportunidade!
