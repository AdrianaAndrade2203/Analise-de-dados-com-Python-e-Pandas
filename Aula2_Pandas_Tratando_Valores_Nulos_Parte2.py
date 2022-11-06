import pandas as pd

df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

print(df1.head())
print(df2.head())
print(df3.head())
print(df4.head())
print(df5.head())

df = pd.concat([df1,df2,df3,df4,df5])

print(df.sample(10))

#Apresentando apenas o que tem valoles nulos na coluna Vendas
print(df[df["Vendas"].isnull()])

#Apresenta tudo que tem valoes nulos no conjunto de dados analisado. (.any). No caso abaixo colocamos para 
#analisar por linha (axis=1)

print(df[df.isnull().any(axis=1)])

print(df.isnull().sum())

#Verificando o valor da media da coluna de Vendas: 
print(df["Vendas"].mean())

#Substituindo os valores nulos por zero 0
df["Vendas"].fillna(0, inplace=True)

print(df.isnull().sum())

#Apagando as linhas com valores nulos
df.dropna(inplace=True)

#Apagando as linhas com valores nulos com base em apenas uma coluna
df.dropna(subset=["Vendas"], inplace=True)

#Apagando as linhas que tiverem valores faltantes em todas as colunas. Apenas se todas as colunas tiverem 
#nulos
df.dropna(how="all", inplace=True)


