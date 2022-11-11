import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

df = pd.read_excel("C:\workspace\Analise de dados com Python e Pandas\Arquivos\AdventureWorks.xlsx")

print(df.head())

print(df.shape)

print(df.dtypes)

#Qual foi a receita total de vendas?
#Basta somar os valores da coluna Valor Venda

print(df["Valor Venda"].sum())

#Para saber o custo total 
#Primeiro vamos criar a coluna de Custos, pois temos no arquivo o custo por unidade a a Quantidade vendida.
#Fazendo a multiplicação dessas colunas sabemos o valor por quantidades vendidas, e na sequencia somando a 
#coluna criada, saberemos os valores totais

df["Custo"] = df["Custo Unitário"].mul(df["Quantidade"])

print(df.head())

print(round(df["Custo"].sum(),2))

#Para saber o Lucro total
#Primeiro vams criar a coluna lucro que sera a receita - custo. E na sequencia fazer a soma das informações
#da nova coluna lucro:

df["Lucro"] = df["Valor Venda"] - df["Custo"]

print(df.head())

print(round(df["Lucro"].sum(),2))

#Temos nas informações as datas de venda e datas do envio. Queremos saber o tempo que levou
#para enviar um determinado produto

df["Tempo_Envio"] = df["Data Envio"] - df["Data Venda"]

print(df.head())

#Verificando o tipo da coluna Tempo_envio

print(df["Tempo_Envio"].dtype)

#Verificando apenas os dias

df["Tempo_Envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

print(df.head())

print(df["Tempo_Envio"].dtype)

#Media do tempo de envio por Marca
print(df.groupby("Marca")["Tempo_Envio"].mean())

#Verificando se temos algum valor faltante em nosso conjunto de dados

print(df.isnull().sum())

#Para saber o lucro por ano e por marca

pd.options.display.float_format = '{:20,.2f}'.format

print(df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum())

lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum().reset_index()

print(lucro_ano)

#Qual o total de produtos vendidos

print(df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False))

#Criando o grafico da informação do total de produtos vendidos
#quando informar bath - será apresentado um grafico de barras horizontais

df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title= "Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto")
plt.show()

#Lucro por ano:
#quando informar apenas bar, ira apresentar um grafico de barras verticais

df.groupby(df["Data Venda"].dt.year)["Lucro"].sum().plot.bar(title= "Lucro X Ano")
plt.xlabel("Ano")
plt.ylabel("Receita");
plt.show()

#Selecionando apenas vendas de 2009

df_2009 = df[df["Data Venda"].dt.year == 2009]
print(df_2009)
print(df_2009.head(6))

#Lucro por mes no ano de 2009
#Se informar apenas .plot o grafico sera de linhas

df_2009.groupby(df["Data Venda"].dt.month)["Lucro"].sum().plot(title= "Lucro X Mes")
plt.xlabel("Mes")
plt.ylabel("Lucro");
plt.show()

#Analise do lucro por Marca

df_2009.groupby("Marca")["Lucro"].sum().plot.bar(title= "Lucro X Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation = "horizontal")
plt.show()

#Lucro por Classe

df_2009.groupby("Classe")["Lucro"].sum().plot.bar(title= "Lucro X Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation = "horizontal")
plt.show()

#Describe = Apresenta algumas analises estatisticas da base

print(df["Tempo_Envio"].describe())

#Grafico de Boxplot
plt.boxplot(df["Tempo_Envio"])
plt.show()

#Histograma
plt.hist(df["Tempo_Envio"])
plt.show()

#Para verificar o tempo de envio minimo com texto:

print("O Tempo de envio minimo é:", df["Tempo_Envio"].min())

#Para verificar o tempo de envio maximo:

print("O Tempo de envio maximo é:", df["Tempo_Envio"].max())

#Identificando o Outlier. Vai apresentar a linha do conjunto de dados que apontou ser a informação isolada
#nos grafios analisados

print(df[df["Tempo_Envio"] == 20])

#Para faze a exportação do CSV da tabela com as alterações que a gente realizou durante a execução da aplicação

df.to_csv("df_vendas_novo_csv")

#Arquivo sem o index:

df.to_csv("df_vendas_novo_csv2", index = False)



