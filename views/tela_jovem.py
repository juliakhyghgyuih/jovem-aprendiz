import tkinter as tk
from tkinter import messagebox, ttk

from views.tela_oportunidades import TelaOportunidades


class TelaJovem:

    def __init__(self, janela, usuario_id, ao_sair=None):
        self.janela = janela
        self.usuario_id = usuario_id
        self.ao_sair = ao_sair
        self.perfil = {
            "nome": "Jovem",
            "email": "demo@evolui.com",
            "cidade": "São Paulo",
            "telefone": "(11) 99999-9999",
            "escolaridade": "Ensino médio",
            "curso": "Informática",
            "habilidades": "Comunicação e organização"
        }
        self.candidaturas_registros = []
        self.tela = tk.Toplevel(janela)
        self.tela.title("Área do Jovem - Evolui")
        self.tela.geometry("760x520")
        self.tela.transient(janela)
        self.tela.focus_set()
        self.tela.protocol("WM_DELETE_WINDOW", self.sair)
        self.criar_interface()

    def criar_interface(self):
        tk.Label(self.tela, text="Área do Jovem", font=("Arial", 22, "bold")).pack(pady=18)
        tk.Label(self.tela, text="Encontre oportunidades e apresente seu potencial.").pack()
        botoes = tk.Frame(self.tela)
        botoes.pack(pady=18)
        tk.Button(botoes, text="Meu perfil", command=self.abrir_perfil, width=20).pack(side="left", padx=5)
        tk.Button(botoes, text="Ver oportunidades", command=self.abrir_oportunidades, width=20).pack(side="left", padx=5)
        tk.Button(botoes, text="Minhas candidaturas", command=self.candidaturas, width=20).pack(side="left", padx=5)
        tk.Button(self.tela, text="Sair", command=self.sair, width=20).pack(pady=8)
        self.resumo = tk.Label(self.tela, text="", justify="left", anchor="w")
        self.resumo.pack(fill="x", padx=35, pady=20)
        self.carregar_perfil()

    def abrir_oportunidades(self):
        self.tela_oportunidades = TelaOportunidades(
            self.tela,
            self.usuario_id,
            ao_sair=self.sair,
            ao_candidatar=self.registrar_candidatura
        )

    def registrar_candidatura(self, oportunidade):
        if not any(item["id"] == oportunidade.id for item in self.candidaturas_registros):
            self.candidaturas_registros.append({
                "id": oportunidade.id,
                "titulo": oportunidade.titulo,
                "empresa": oportunidade.empresa
            })

    def carregar_perfil(self):
        self.resumo.config(
            text=f"Olá, {self.perfil['nome']}!\n"
                 f"Cidade: {self.perfil['cidade']}\n"
                 f"Escolaridade: {self.perfil['escolaridade']}"
        )

    def abrir_perfil(self):
        PerfilJovem(self.tela, self.usuario_id, self.carregar_perfil, self.perfil)

    def candidaturas(self):
        janela = tk.Toplevel(self.tela)
        janela.title("Minhas candidaturas")
        janela.geometry("560x300")
        tk.Label(janela, text="Minhas candidaturas", font=("Arial", 18, "bold")).pack(pady=18)
        if not self.candidaturas_registros:
            tk.Label(janela, text="Você ainda não tem candidaturas.").pack(pady=20)
            return
        for candidatura in self.candidaturas_registros:
            tk.Label(
                janela,
                text=f"{candidatura['titulo']} | {candidatura['empresa']} | Status: Realizada",
                anchor="w"
            ).pack(fill="x", padx=25, pady=4)

    def sair(self):
        if self.ao_sair is not None:
            self.ao_sair()
        self.tela.destroy()


class PerfilJovem:

    def __init__(self, janela, usuario_id, ao_salvar, perfil=None):
        self.ao_salvar = ao_salvar
        self.perfil = perfil or {
            "nome": "Jovem",
            "email": "demo@evolui.com",
            "cidade": "São Paulo",
            "telefone": "(11) 99999-9999",
            "escolaridade": "Ensino médio",
            "curso": "Informática",
            "habilidades": "Comunicação e organização"
        }
        self.tela = tk.Toplevel(janela)
        self.tela.title("Meu perfil")
        self.tela.geometry("460x500")
        self.campos = {}
        for chave, rotulo in (("nome", "Nome"), ("cidade", "Cidade"), ("telefone", "Telefone"), ("email", "E-mail"), ("escolaridade", "Escolaridade"), ("curso", "Cursos"), ("habilidades", "Habilidades")):
            tk.Label(self.tela, text=rotulo).pack(anchor="w", padx=25, pady=(7, 0))
            campo = tk.Entry(self.tela, width=48)
            campo.insert(0, self.perfil.get(chave) or "")
            campo.pack(padx=25)
            self.campos[chave] = campo
        tk.Button(self.tela, text="Salvar perfil", command=self.salvar, width=20).pack(pady=18)

    def salvar(self):
        valores = {chave: campo.get().strip() for chave, campo in self.campos.items()}
        if not valores["nome"] or not valores["email"]:
            messagebox.showwarning("Atenção", "Nome e e-mail são obrigatórios.")
            return
        self.perfil.update(valores)
        messagebox.showinfo("Sucesso", "Perfil salvo com sucesso!")
        self.ao_salvar()
        self.tela.destroy()
