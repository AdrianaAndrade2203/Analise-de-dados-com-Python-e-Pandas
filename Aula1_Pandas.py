#Parte do codigo abaixo comentado, foi utilizado para abrir o arquivo antes de implortar a biblioteca pandas,
# e testar se o local e nome do arquivo estavam corretos e o arquivo abrindo devidamente

#arquivo = open ("Gapminder.csv")
#print(arquivo.read())

#para importar a biblioteca pandas
#Eu nao tinha a biblioteca baixada, sendo assim precisei instalar, pois na aula a professora usou o 
#Google Colab, que ja possui algumas funcionalidades automaticamente no Jupyter, e eu tive preferencia de usar
#o VSCode, por ter mais familiaridade e configurações automatizadas para deploy dos projetos no meu GitHub
#Para baixar a biblioteca pandas, basta abrir o CMD e executar o comando "pip install pandas"

import pandas as pd

#para ler um  arquivo em CSV
df = pd.read_csv("C:\workspace\Analise de dados com Python e Pandas\Arquivos\Gapminder.csv",
error_bad_lines = False, sep=";")

#para visualizar as 10 primeiras linhas dos arquivos. Caso nada seja digitado entre parenteses por Default, 
#serão apresentadas as 5 primeiras linhas
print(df.head(10))

#Para renomear o nome das colunad
df = df.rename(columns={"country":"Pais", "continent":"Continente", "year":"Ano", 
"lifeExp":"Expectativa de vida", "pop":"Populacao", "gdpPercap":"PIB"})

print(df)

print(df.head(10))

#Para saber o total de linhas e colunas que temos
print(df.shape)

#Para retornar o nome das colunas

print(df.columns)

#Para retornar o tipo de dados armazenado em cada coluna

print(df.dtypes)

#apresenta as ultimas linhas que foram mencionadas dentro dos (). Se nao informar nada, traz as ultimas 5
print(df.tail())

#Retorna informações estatisticas do conjunto de dados que estamos analisando
print(df.describe())


#Imprime as possiveis informações que tem na coluna mencionada. No exemplo abaixo, em continentes
print(df["Continente"].unique())

Oceania = df.loc[df["Continente"] == "Oceania"]
Oceania.head()
print(Oceania)

#Agrupamento de Dados (groupy by)

print(df.groupby("Continente")["Pais"].nunique())

#Qual expectativa de vida media para cada ano?:

print(df.groupby("Ano")["Expectativa de vida"].mean())

#Media do PIB
print(df["PIB"].mean())

#Soma da coluna informada
print(df["PIB"].sum())
