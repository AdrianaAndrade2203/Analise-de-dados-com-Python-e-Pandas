
import pandas as pd

import os
for f in os.listdir("C:\workspace\Analise de dados com Python e Pandas\Arquivos"):
	print(f)

df1 = pd.read_excel("C:\workspace\Analise de dados com Python e Pandas\Arquivos\_Aracaju.xlsx")
df2 = pd.read_excel("C:\workspace\Analise de dados com Python e Pandas\Arquivos\Fortaleza.xlsx")
df3 = pd.read_excel("C:\workspace\Analise de dados com Python e Pandas\Arquivos\_Natal.xlsx")
df4 = pd.read_excel("C:\workspace\Analise de dados com Python e Pandas\Arquivos\Recife.xlsx")
df5 = pd.read_excel("C:\workspace\Analise de dados com Python e Pandas\Arquivos\Salvador.xlsx")


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

#Substituindo os valores nulos pela media de valores da coluna
df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

print(df.isnull().sum())

print(df["Vendas"].mean())

