import os

# Mostra o diretório atual onde o Python está rodando
diretorio_atual = os.getcwd()
print(f"\n📂 Diretório atual: {diretorio_atual}\n")

# Lista todos os arquivos desse diretório
arquivos = os.listdir(diretorio_atual)

print("🗂️ Arquivos encontrados na pasta:\n")
for arquivo in arquivos:
    print(arquivo)

# Verifica se os PDFs estão presentes
if 'folha de pagamento.pdf' in arquivos and 'folha de pagamento atualizada.pdf' in arquivos:
    print("\n✅ Os dois arquivos PDF estão na pasta corretamente!")
else:
    print("\n⚠️ Atenção! Algum dos PDFs não foi encontrado na pasta!")
