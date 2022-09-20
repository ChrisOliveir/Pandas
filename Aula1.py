from sys import displayhook
from tkinter.tix import DisplayStyle
import pandas as pd 

# lendo arquivo CSV 
# as vezes precisaremos mudar o encoding, possiveis valores para testar:
# encoding='Latin1', encoding='ISO-8859-1',' encoding='utf-8' ou encoding='cp1252'

vendas_df = pd.read_csv('Vendas.csv', sep=";")
produtos_df = pd.read_csv('Cadastro Produtos.csv', sep=";")
lojas_df = pd.read_csv('Lojas.csv', sep=";")
clientes_df = pd.read_csv('Clientes.csv', sep=";")
print(vendas_df.info()) 
 
 #escolhendo colunas que quero pegar
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

#juntando os dataframes 
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on="ID Cliente")



# renomeando o nome da coluna e-mail 
vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do Cliente'})

#exibindo o dataframe final 
displayhook(vendas_df)

#exibindo as tabelas 
#displayhook(produtos_df)
#displayhook(lojas_df)
#displayhook(clientes_df)