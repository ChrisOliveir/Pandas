from sys import displayhook
from tkinter.tix import DisplayStyle
import pandas as pd 
import matplotlib.pyplot as plt

# lendo arquivo CSV 
# as vezes precisaremos mudar o encoding, possiveis valores para testar:
# encoding='Latin1', encoding='ISO-8859-1',' encoding='utf-8' ou encoding='cp1252'

vendas_df = pd.read_csv('Vendas.csv', sep=";")
produtos_df = pd.read_csv('Cadastro Produtos.csv', sep=";")
lojas_df = pd.read_csv('Lojas.csv', sep=";")
clientes_df = pd.read_csv('Clientes.csv', sep=";")
#print(vendas_df.info()) 
 
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

#qual cliente comprou mais vezes?

frequencia_clientes = vendas_df['E-mail do Cliente'].value_counts()
frequencia_clientes.plot()
#plt.show()

#QUAL LOJA MAIS  VENDEU?
#usaremos o .GROUPBY para agrupar o nosso dataframe

vendas_lojas = vendas_df.groupby('Nome da Loja').sum() #juntou as lojas e somou os valores 
#print(vendas_lojas)

#ordenando o dataframe 

vendas_lojas = vendas_lojas.sort_values('Quantidade Vendida') #ordenando do menor pra o maior 
vendas_lojas = vendas_lojas.sort_values('Quantidade Vendida', ascending=False) #ordenando do maior para o menor
#print(vendas_lojas)

#queremos fazer analise somente para a loja contoso europe online e saber o % de devolução dessa loja

vendas_lojacontosoeurope = vendas_df[vendas_df['ID Loja'] == 306]
qtd_vendida = vendas_lojacontosoeurope['Quantidade Vendida'].sum()
qtd_devolvida = vendas_lojacontosoeurope['Quantidade Devolvida'].sum()
print('{:.2%}'.format(qtd_devolvida/qtd_vendida))
