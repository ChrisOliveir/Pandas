import pyodbc 
import numpy as np
import pandas as pd 


dados_conexao = ("Driver={SQLite3 ODBC Driver}; Server=localhost; Database=chinook.db")

# caso precise de login e senha :
#dados_conexão = ("Driver={meu drive}; Server= meuservidor; Database=NomeBaseDeDados;
# UID= Login; PWD= Senha;")

conexao = pyodbc.connect(dados_conexao)
print("ok")

cursor = conexao.cursor() # o cursor é o cara que comanda a integração do banco com o pyobdc

cursor.execute("SELECT * FROM customers")  # leia todas as informações da tabela Customers

valores = cursor.fetchall() # esta armazenando as iformações dentro da variavel valor no formato de uma lista de tuplas
# print(valores[0]) # primeiro 10 valores

cursor.close()
tabela_clientes = pd.DataFrame.from_records(valores)


