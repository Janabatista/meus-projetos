import pandas as pd
data={
    "tipo de aposentadoria":[
        'invalidez',
        'invalidez',
        'invalidez',
        'tempo de contribuição',
        'tempo de contribuição',
        'tempo de contribuição',
        'tempo de contribuição',
        'tempo de contribuição',
        'invalidez',
    ],
    "Paridade":[
        'paridade',
        'paridade',
        'paridade',
        'paridade',
        'paridade',
        'paridade',
        'paridade',
        'paridade',
        'sem paridade',
    ],
    "Data de admissão":[
        '17/02/2003',
        '03/11/1999',
        '01/06/1999',
        '03/01/1994',
        '01/02/1994',
        '01/03/2003',
        '01/05/2000',
        '11/09/1995',
        '03/08/1998',

    ]

}
df = pd.DataFrame(data)

# Exportar para um arquivo Excel
output_path = "aposentadoria_dependentes.xlsx"
df.to_excel(output_path, index=False)

print(f"Arquivo Excel salvo em: {output_path}")
