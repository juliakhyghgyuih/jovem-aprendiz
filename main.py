import tkinter as tk
from tkinter import messagebox
from views.cadastro import TelaCadastro
from views.login import TelaLogin
from views.tela_empresa import TelaEmpresa
from views.tela_jovem import TelaJovem
from views.tela_oportunidades import TelaOportunidades
from sessao import Sessao


class Evolui:

    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Evolui")
        self.janela.geometry("500x400")
        self.sessao = Sessao()

        self.criar_interface()

    def criar_interface(self):

        titulo = tk.Label(
            self.janela,
            text="EVOLUI",
            font=("Arial", 28, "bold")
        )
        titulo.pack(pady=40)

        frase = tk.Label(
            self.janela,
            text="Conectando jovens a empresas e novas oportunidades.",
            font=("Arial", 12)
        )
        frase.pack(pady=10)

        botao_jovem = tk.Button(
            self.janela,
            text="Entrar",
            width=20,
            command=self.abrir_login
        )
        botao_jovem.pack(pady=10)

        botao_empresa = tk.Button(
            self.janela,
            text="Sou Empresa",
            width=20,
            command=self.abrir_login_empresa
        )
        botao_empresa.pack(pady=10)

        botao_sair = tk.Button(
            self.janela,
            text="Sair",
            width=20,
            command=self.janela.destroy
        )
        botao_sair.pack(pady=10)

    def abrir_cadastro(self):
        try:
            self.janela.update()
            tela = TelaCadastro(self.janela)
            if hasattr(tela, 'tela'):
                tela.tela.transient(self.janela)
                tela.tela.grab_set()
                tela.tela.focus_set()
        except Exception as erro:
            messagebox.showerror(
                "Erro",
                f"Não foi possível abrir a tela de cadastro:\n{erro}"
            )

    def abrir_login(self):
        try:
            self.janela.update()
            self.tela_login = TelaLogin(self.janela, self.abrir_area_usuario)
            if hasattr(self.tela_login, 'tela'):
                self.tela_login.tela.transient(self.janela)
                self.tela_login.tela.grab_set()
                self.tela_login.tela.focus_set()
        except Exception as erro:
            messagebox.showerror(
                "Erro",
                f"Não foi possível abrir a tela de login:\n{erro}"
            )

    def abrir_login_empresa(self):
        try:
            self.janela.update()
            self.tela_login = TelaLogin(
                self.janela,
                self.abrir_area_usuario,
                tipo_inicial="Empresa"
            )
            self.tela_login.tela.transient(self.janela)
            self.tela_login.tela.grab_set()
            self.tela_login.tela.focus_set()
        except Exception as erro:
            messagebox.showerror(
                "Erro",
                f"Não foi possível abrir a tela de login:\n{erro}"
            )

    def abrir_area_usuario(self, usuario):
        self.sessao.iniciar(usuario)
        if self.sessao.tipo == "empresa":
            self.abrir_empresa()
        else:
            self.tela_jovem = TelaJovem(
                self.janela,
                self.sessao.usuario_id,
                ao_sair=self.encerrar_sessao
            )

    def abrir_empresa(self, usuario_id=None):
        try:
            self.janela.update()
            self.tela_empresa = TelaEmpresa(self.janela, self.sessao, self.encerrar_sessao)
            self.tela_empresa.tela.transient(self.janela)
            self.tela_empresa.tela.grab_set()
            self.tela_empresa.tela.focus_set()
        except Exception as erro:
            messagebox.showerror(
                "Erro",
                f"Não foi possível abrir a área da empresa:\n{erro}"
            )

    def encerrar_sessao(self):
        self.sessao.encerrar()

    def abrir_area_jovem(self, usuario_id):
        """Mantem compatibilidade com chamadas antigas do fluxo jovem."""
        self.tela_jovem = TelaJovem(
            self.janela,
            usuario_id,
            ao_sair=self.encerrar_sessao
        )

    def iniciar(self):
        self.janela.mainloop()


if __name__ == "__main__":
    app = Evolui()
    app.iniciar()