
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

#Para fazar a junção de todos os aruivos. Usar o concat

df = pd.concat([df1,df2,df3,df4,df5])

#Verificando o tipo de data de cada coluna

print(df.dtypes)

#Alterando o tipo de dado da coluna Data para tipo inteiro
df["Data"] = df["Data"].astype("int64")

print(df.dtypes)


#Alterando o tipo de dado da coluna Data para tipo Datatime

df["Data"] = pd.to_datetime(df["Data"])

print(df.dtypes)

#Criando novas colunas:
#Neste caso vamos criar uma coluna de receitas (vendas x Qtd). Mul (de multiplicação)

df["Receita"] = df["Vendas"].mul(df["Qtde"])

print(df.head())

print(df.dtypes)

#Agrupamento por ano
print(df.groupby(df["Data"].dt.year)["Receita"].sum())

#Criando uma nova coluna com o ano

df["Ano_Venda"] = df["Data"].dt.year

print(df.sample(5))


#Extraindo o mês e o dia da venda. Criando as colunas pos mês e dia

df["Mes_Venda"], df["Dia_Venda"] = (df["Data"].dt.month, df["Data"].dt.day)

print(df.sample(5))

#Retornando a Data mais antiga

print(df["Data"].min())

#Calculando a diferença de dias (na mesma coluna) e criando uma nova coluna para essa informação

df["Diferenca_Dias"] = df["Data"] - df["Data"].min()
print(df.sample(5))

#Criando uma coluna de trimestre

df["Trimestre_Venda"] = df["Data"].dt.quarter
print(df.sample(5))

#Filtrando as vendas de 2019 e do mes de março. (Buscando um Subconjunto)

vendas_marco_2019 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]

print(vendas_marco_2019)


