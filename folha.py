import pdfplumber
import pandas as pd
import re
import os

# Função para extrair dados dos PDFs
def extrair_dados(pdf_path):
    dados = []

    with pdfplumber.open(pdf_path) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()

            if texto:
                linhas = texto.split('\n')

                for linha in linhas:
                    match = re.search(r'FUNCIONARIO:\s*(\d+)\s+(.*)Nivel Sal:\s*(\d+)\s+Salario\s*:\s*([\d.,]+)', linha)

                    if match:
                        matricula = match.group(1).strip()
                        nome = match.group(2).strip()
                        nivel = match.group(3).strip()
                        salario = float(match.group(4).replace('.', '').replace(',', '.'))

                        dados.append({
                            'Matricula': matricula,
                            'Nome': nome,
                            'Nivel': nivel,
                            'Salario': salario
                        })

    return pd.DataFrame(dados)


# Definir os PDFs
pdf1 = r"folha1.pdf"
pdf2 = r"folha2.pdf"

# Extrair dados
df1 = extrair_dados(pdf1)
df2 = extrair_dados(pdf2)

print("\n🔍 Dados extraídos com sucesso!")

# Comparação
comparacao = pd.merge(df1, df2, on='Matricula', suffixes=('_folha1', '_folha2'), how='outer', indicator=True)

# Diferenças nos salários
dif_salario = comparacao[comparacao['Salario_folha1'] != comparacao['Salario_folha2']]

# Funcionários que entraram ou saíram
entraram = comparacao[comparacao['_merge'] == 'right_only']
sairam = comparacao[comparacao['_merge'] == 'left_only']

# 🚩 Mensagens inteligentes
if not dif_salario.empty:
    print("\n⚠️ Diferenças de salário encontradas!")
    print(dif_salario[['Matricula', 'Nome_folha1', 'Salario_folha1', 'Salario_folha2']])
else:
    print("\n✅ Não há diferenças nos salários.")

if not entraram.empty:
    print("\n🚦 Funcionários que entraram na folha:")
    print(entraram[['Matricula', 'Nome_folha2']])
else:
    print("\n✅ Nenhum funcionário novo na folha.")

if not sairam.empty:
    print("\n🚦 Funcionários que saíram da folha:")
    print(sairam[['Matricula', 'Nome_folha1']])
else:
    print("\n✅ Nenhum funcionário saiu da folha.")

# 🗂️ Exportar Excel
with pd.ExcelWriter('comparativo_folha.xlsx') as writer:
    comparacao.to_excel(writer, sheet_name='Comparacao_Completa', index=False)
    dif_salario.to_excel(writer, sheet_name='Diferenca_Salario', index=False)
    entraram.to_excel(writer, sheet_name='Entraram', index=False)
    sairam.to_excel(writer, sheet_name='Sairam', index=False)

print("\n📄 Arquivo gerado: comparativo_folha.xlsx")
