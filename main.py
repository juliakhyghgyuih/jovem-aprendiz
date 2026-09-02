import tkinter as tk
from views.cadastro import TelaCadastro


class Evolui:

    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Evolui")
        self.janela.geometry("500x400")

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
            text="Cresça por dentro. Avance por fora.",
            font=("Arial", 12)
        )
        frase.pack(pady=10)

        botao_entrar = tk.Button(
            self.janela,
            text="Entrar",
            width=20
        )
        botao_entrar.pack(pady=10)

        botao_cadastrar = tk.Button(
            self.janela,
            text="Cadastrar",
            width=20,
            command=self.abrir_cadastro
        )
        botao_cadastrar.pack(pady=10)

        botao_sair = tk.Button(
            self.janela,
            text="Sair",
            width=20,
            command=self.janela.destroy
        )
        botao_sair.pack(pady=10)

    def abrir_cadastro(self):
        TelaCadastro(self.janela)

    def iniciar(self):
        self.janela.mainloop()


if __name__ == "__main__":
    app = Evolui()
    app.iniciar()