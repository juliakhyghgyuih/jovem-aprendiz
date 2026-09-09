import tkinter as tk
from tkinter import messagebox


class TelaLogin:

    def __init__(self, janela, ao_entrar=None, tipo_inicial=None):
        self.janela = janela
        self.ao_entrar = ao_entrar
        self.tipo_inicial = tipo_inicial.strip().lower() if tipo_inicial else None

        self.tela = tk.Toplevel(janela)
        titulo_tipo = " como Empresa" if self.tipo_inicial == "empresa" else ""
        self.tela.title(f"Entrar{titulo_tipo} - Evolui")
        self.tela.geometry("400x300")
        self.tela.transient(janela)
        self.tela.grab_set()
        self.tela.focus_set()
        self.tela.lift()

        titulo = tk.Label(
            self.tela,
            text="Entrar",
            font=("Arial", 22, "bold")
        )
        titulo.pack(pady=25)

        tk.Label(self.tela, text="E-mail:").pack()
        self.email = tk.Entry(self.tela, width=35)
        self.email.pack(pady=5)

        tk.Label(self.tela, text="Senha:").pack()
        self.senha = tk.Entry(self.tela, width=35, show="*")
        self.senha.pack(pady=5)

        tk.Button(
            self.tela,
            text="Entrar como Jovem",
            width=20,
            command=lambda: self.entrar("jovem")
        ).pack(pady=12)

        tk.Button(
            self.tela,
            text="Entrar como Empresa",
            width=20,
            command=lambda: self.entrar("empresa")
        ).pack(pady=4)

        tk.Button(
            self.tela,
            text="Ainda não tenho cadastro",
            command=self.abrir_cadastro
        ).pack()

    def entrar(self, tipo=None):
        tipo = tipo or self.tipo_inicial or "jovem"
        usuario = {
            "id": 1 if tipo == "jovem" else 2,
            "nome": "Jovem" if tipo == "jovem" else "Empresa Exemplo",
            "email": self.email.get().strip() or "demo@evolui.com",
            "tipo": tipo
        }
        if self.ao_entrar is not None:
            self.ao_entrar(usuario)
        self.tela.destroy()

    def abrir_cadastro(self):
        from views.cadastro import TelaCadastro

        TelaCadastro(self.tela, tipo_inicial=self.tipo_inicial)
