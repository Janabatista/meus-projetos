from PyPDF2 import PdfReader
import pandas as pd
import re

# Carregar o PDF
file_path = r"D:\Usuario\Área de Trabalho\automação\aposentadoriaidade.pdf"
pdf = PdfReader(file_path)

# Definir padrões de regex para capturar informações específicas
patterns = {
    'Nome': r'Funcionário.....:\s*\d+\s*-\s*([A-Z\s]+)',
    'Matrícula': r'Funcionário.....:\s*(\d+)',
    'CPF': r'CPF:\s*(\d{3}\.\d{3}\.\d{3}-\d{2})',
    'PIS/PASEP': r'PIS/PASEP:\s*(\d+)',
    'Sexo': r'Sexo:\s*([MF])',
    'Estado Civil': r'Estado Civil....:\s*([A-Za-z]+)',
    'Data de Nascimento': r'Data Nascimento.:\s*(\d{2}/\d{2}/\d{4})',
    'Situação Funcional': r'Vinculo.........:\s*(\d+)\s*-\s*([A-Za-z\s]+)',
    'Data de Admissão': r'Data Admissão...:\s*(\d{2}/\d{2}/\d{4})',
    'Cargo': r'Cargo/Função....:\s*\d+\s*-\s*([A-Za-z\s]+)',
    'Remuneração Bruta': r'Salário:\s*([\d.,]+)'
}




# Inicializar uma lista para armazenar as informações extraídas
data = []

# Extrair texto de cada página do PDF e aplicar regex para capturar os dados
for page in pdf.pages:
    text = page.extract_text()
    record = {}
    for field, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            record[field] = match.group(1).strip()
        else:
            record[field] = None
    # Somente adicionar registros completos (com Nome) na lista
    if record.get('Nome'):
        data.append(record)

# Criar um DataFrame com os dados extraídos
df = pd.DataFrame(data)

# Salvar o DataFrame em um arquivo Excel
output_path = r"D:\Usuario\Área de Trabalho/idade_relatorio.xlsx"
df.to_excel(output_path, index=False)
