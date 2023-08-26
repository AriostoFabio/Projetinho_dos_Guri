import sqlite3
import tkinter as tk

from tkinter import messagebox

con = sqlite3.connect("tutorial.db")

# Conectando ao banco de dados (será criado se não existir)
con = sqlite3.connect('usuarios.db')
cursor = con.cursor()

# Criando a tabela 'usuarios'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        id_usuario INTEGER,
        nome TEXT,
        senha TEXT,
        email TEXT,
        FOREIGN KEY (id_usuario) REFERENCES usuarios (id)
    )
''')

# Criando um cursor para executar comandos SQL

# Inserindo alguns registros na tabela
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES('joao', 29)")
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES('shakira', 23)")

# Salvando as alterações e fechando a conexão
con.commit()

# Fazendo uma consulta simples e imprimindo os resultados
cursor.execute('SELECT * FROM usuarios')
for row in cursor.fetchall():
    print(row)

def check_credentials():
    name = name_entry.get()
    senha = pass_entry.get()
    
    adm_name = 'Fabio'
    adm_pass = '1234'
    
    if name == adm_name and senha == adm_pass:
        messagebox.showinfo('Sucesso', 'Acesso liberado!')
    else:
        messagebox.showwarning('Erro', 'Acesso negado BITCH!')

# Criar janela principal
root = tk.Tk()
root.title("Login")
root.geometry("300x500")

# Criar um frame central para conter todos os widgets
center_frame = tk.Frame(root)
center_frame.place(relx=0.5, rely=0.5, anchor='center')

# Label e Entry para o nome de usuário dentro do center_frame
name_label = tk.Label(center_frame, text="Usuário:")
name_label.pack(pady=5)

name_entry = tk.Entry(center_frame)
name_entry.pack(pady=5)

# Label e Entry para a senha dentro do center_frame
pass_label = tk.Label(center_frame, text="Senha:")
pass_label.pack(pady=5)

pass_entry = tk.Entry(center_frame, show='*')  # show='*' oculta a senha
pass_entry.pack(pady=5)

# Botão de login dentro do center_frame
login_button = tk.Button(center_frame, text="Login", command=check_credentials)
login_button.pack(pady=10)

root.mainloop()

# Fechando a conexão
con.close()