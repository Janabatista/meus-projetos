import pandas as pd

# Criando uma estrutura para armazenar os dados extraídos
data = {
    "Nome do Declarante": [
        "MARCIO JULIANO BORGES COSTA",
        "EITOR DA SILVA QUADROS",
        "JOSE BENEDITO RAIMUNDO",
        "MARIA APARECIDA DE ASSIS",
        "ELISVAINI NUNES DA SILVA",
        "MAVELITA ENGEL PRESTES"
    ],
    "CPF do Declarante": [
        "616.756.522-87",
        "337.628.219-68",
        "209.305.009-97",
        "575.545.602-04",
        "242.114.002-15",
        "606.109.052-87"
    ],
    "Matrícula do Declarante": [
        "297",
        "168",
        "326",
        "270",
        "283",
        "276"
    ],
    "Sexo do Declarante": [
        "SOLTEIRA(O)",
        "SOLTEIRA(O)",
        "CASADA(O)",
        "SOLTEIRA(O)",
        "SOLTEIRA(O)",
        "SOLTEIRA(O)"
    ],
    "Nome do Dependente": [
        "VICTOR JOAQUIM VARGAS COSTA",
        "JOICY BRUNO QUADROS",
        "VALDECIR SCHINK RAIMUNDO",
        "SAMUEL ASSIS DE PAULO",
        "MARIA LAURA CESPEDES DA SILVA",
        "ALAN DANIEL ENGEL DA SILVA"
    ],
    "CPF do Dependente": [None, None, None, None, None, None],
    "Data de Nascimento do Dependente": [
        "12/04/2008",
        "28/07/2003",
        "01/09/1959",
        "01/12/2007",
        "10/07/2007",
        "14/08/2008"
    ],
    "Sexo do Dependente": ["Filha(o)", "Filha(o)", "Esposa(o)", "Filha(o)", "Filha(o)", "Filha(o)"],
    "Parentesco": [
        "Filha(o)",
        "Filha(o)",
        "Esposa(o)",
        "Filha(o)",
        "Filha(o)",
        "Filha(o)"
    ]
}

# Criar um DataFrame com os dados
df = pd.DataFrame(data)

# Exportar para um arquivo Excel
output_path = "declarantes_dependentes.xlsx"
df.to_excel(output_path, index=False)

print(f"Arquivo Excel salvo em: {output_path}")
