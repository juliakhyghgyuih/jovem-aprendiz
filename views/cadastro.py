import tkinter as tk
from tkinter import messagebox, ttk



class TelaCadastro:

    def __init__(self, janela, tipo_inicial=None):
        self.janela = janela
        self.tipo_inicial = tipo_inicial.strip().lower() if tipo_inicial else None

        self.tela = tk.Toplevel(janela)
        self.tela.title("Cadastro - Evolui")
        self.tela.geometry("400x460")
        self.tela.transient(janela)
        self.tela.grab_set()
        self.tela.focus_set()
        self.tela.lift()
        self.tela.attributes("-topmost", True)
        self.tela.after(100, lambda: self.tela.attributes("-topmost", False))

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

        tk.Label(self.tela, text="Tipo de usuário:").pack()
        self.tipo = tk.StringVar(value=self.tipo_inicial or "jovem")
        estado_tipo = "disabled" if self.tipo_inicial in ("jovem", "empresa") else "readonly"
        ttk.Combobox(self.tela, textvariable=self.tipo, values=("jovem", "empresa"), state=estado_tipo, width=32).pack(pady=5)

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
        tipo = self.tipo.get()

        if nome == "" or email == "" or senha == "" or tipo == "":
            messagebox.showwarning(
                "Atenção",
                "Preencha todos os campos."
            )
            return

        messagebox.showinfo(
            "Sucesso",
            "Cadastro demonstrativo realizado com sucesso!"
        )
        self.tela.destroy()