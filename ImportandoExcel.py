import pandas as pd
excel = pd.read_excel("Vendedor.xlsx")

#variável mês para controlar o fluxo de vendas dos meses
mes = input('Qual mês você quer analizar? ')

#retorna a analise do vendedor que mais vendeu

#ordena o mês

analise = excel.sort_values(by=f'{mes}' ,ascending=False)
print(analise)


#só quero o vendedor, como ele está na 1 coluna: [0][0]
print(analise.iloc[0][0])

#melhorando...
print(f'O melhor vendedor do mês de {mes} foi o(a) {analise.iloc[0][0]} ')

#quem menos vendeu
analise = excel.sort_values(by=f'{mes}' ,ascending=True)
print(f'O pior vendedor do mês de {mes} foi o(a) {analise.iloc[0][0]} ')


