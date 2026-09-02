import tkinter as tk
from tkinter import messagebox

from models.usuario import Usuario
from conexao import conectar


class TelaCadastro:

    def __init__(self, janela):
        self.janela = janela

        self.tela = tk.Toplevel(janela)
        self.tela.title("Cadastro - Evolui")
        self.tela.geometry("400x400")

        titulo = tk.Label(
            self.tela,
            text="Cadastro",
            font=("Arial", 22, "bold")
        )
        titulo.pack(pady=20)

        tk.Label(self.tela, text="Nome:").pack()
        self.nome = tk.Entry(self.tela, width=35)
        self.nome.pack(pady=5)

        tk.Label(self.tela, text="E-mail:").pack()
        self.email = tk.Entry(self.tela, width=35)
        self.email.pack(pady=5)

        tk.Label(self.tela, text="Senha:").pack()
        self.senha = tk.Entry(self.tela, width=35, show="*")
        self.senha.pack(pady=5)

        botao = tk.Button(
            self.tela,
            text="Cadastrar",
            width=20,
            command=self.cadastrar
        )
        botao.pack(pady=20)

    def cadastrar(self):
        nome = self.nome.get()
        email = self.email.get()
        senha = self.senha.get()

        if nome == "" or email == "" or senha == "":
            messagebox.showwarning(
                "Atenção",
                "Preencha todos os campos."
            )
            return

        usuario = Usuario(nome, email, senha)
        conexao = None
        cursor = None

        try:
            conexao = conectar()
            cursor = conexao.cursor()

            sql = """
                INSERT INTO usuarios (nome, email, senha)
                VALUES (%s, %s, %s)
            """

            valores = (
                usuario.nome,
                usuario.email,
                usuario.senha
            )

            cursor.execute(sql, valores)
            conexao.commit()

            messagebox.showinfo(
                "Sucesso",
                "Usuário cadastrado com sucesso!"
            )

            self.tela.destroy()

        except Exception as erro:
            messagebox.showerror(
                "Erro",
                f"Não foi possível cadastrar:\n{erro}"
            )
        finally:
            if cursor is not None:
                cursor.close()
            if conexao is not None and conexao.is_connected():
                conexao.close()