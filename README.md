# Projetinho_dos_Guri


#TODO Tarefa 1:
Favor de lembrar de executar a venv!
Utilize a seguinte documentação como referência: https://docs.python.org/3/library/sqlite3.html, a fim de estabelecer a estrutura de correspondência com os dados de login. 
A estrutura atual pode ser reaproveitada para implementar o processo de acesso. 


Após completar esta etapa, considere a possibilidade de adicionar um procedimento para criar o banco de dados com as tabelas embutidas, caso ele não seja encontrado.
>> Exemplo:
cur.execute()
com o script de database no exista:
""" CREATE TABLE IF NOT EXISTS nome_da_tabela (
    coluna1 tipo_de_dado,
    coluna2 tipo_de_dado,
    ...,
    PRIMARY KEY (coluna1)
);
"""
Vai ser ser necessario criar este tratamento para evitar caso haja delete, pois criara sempre os dados de estrutura para a criação de uma base nova.
Futuramente pensaremos como fazer backup de sincronização para evitar este tipo de problema.