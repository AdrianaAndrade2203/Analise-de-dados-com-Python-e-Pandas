#Para fazer importações de arquivos do tipo .xlsx pela biblioteca pandas, foi necessária a instalação 
#do modulo módulo openpyxl. Neste caso abra o CMD e execute o comando "pip install openpyxl"

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

#Para fazar a junção de todos os aruivos. Usar o concat

df = pd.concat([df1,df2,df3,df4,df5])

#Para verificar o arquivo após a junção. O head apresenta as primeiras 5 linhas. Se quiser mais, basta informar 
#a quantidade de linhas entre aspas
print(df.head())


#Para verificar o arquivo após a junção. O tail apresenta as ultimas 5 linhas. Se quiser mais, basta informar 
#a quantidade de linhas entre aspas
print(df.tail())

#Para verificar o arquivo após a junção. O sample apresenta uma amostra do arquivo. 
#Basta informar a quantidade de linhas entre aspas

print(df.sample(10))

#para apresentar os tipos de dados que temos no arquivo

print(df.dtypes)

#Alterando o tipo de dado de um coluna. No exemplo iremos alterar a coluna LojaID

df["LojaID"] = df["LojaID"].astype("object")

#Após a alteração, verificando os tipos de dados novamente:

print(df.dtypes)

#Tratando Valores faltantes nos concjuntos de dados
#Consultando valores faltantes. No caso de usarmos o sum, estamos referenciando que se encontrar valores
#nulos, trazer a soma deles de cada coluna que temos

print(df.isnull().sum())

#Substituindo os valores nulos que foram encontrados acima, pela média
df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

#Substituindo os valores nulos que foram encontrados acima, por zero
df["Vendas"].fillna(0, inplace=True)


print(df.isnull().sum())

#Verificando o valor da media da coluna Vendas

print(df["Vendas"].mean())

print(df.sample(20))

#Criando novas colunas:
#Neste caso vamos criar uma coluna de receitas (vendas x Qtd). Mul (de multiplicação)

df["Receita"] = df["Vendas"].mul(df["Qtde"])

print(df.head())

#Se por acaso eu ja tivesse a receita, porem nao tivesse  quantidade eu poderia fazer a divisão

df["Receita/Vendas"] = df["Receita"] / (df["Vendas"])

print(df.head())

#Retornando a maior informação da Coluna Receita
print(df["Receita"].max())

#Ordenando os valores em ordem crescente pela coluna receita
df.sort_values(by=["Receita"], inplace=True)

print(df.head())

#Retornando a menor informação da Coluna Receita
print(df["Receita"].min())

#Retornando as 3 maiores receitas:
print(df.nlargest(3, "Receita"))

#Retornando as 10 menores receitas:
print(df.nsmallest(10, "Receita"))

#Agrupamento por cidade. Retornando a soma da receita por cidade. Ou seja agrupamos o campo cidade, para saber
#quanto temos de receita por cada cidade

print(df.groupby("Cidade")["Receita"].sum())

#Outra forma de Ordenar os valores em ordem crescente pela coluna receita

print(df.sort_values("Receita", ascending=False).head(10))
