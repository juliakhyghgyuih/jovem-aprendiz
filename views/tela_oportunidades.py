import tkinter as tk
from tkinter import messagebox, ttk

from models.oportunidade import Oportunidade


class TelaOportunidades:

    def __init__(self, janela, usuario_id=None, sessao=None, ao_sair=None, ao_candidatar=None):
        self.janela = janela
        self.sessao = sessao
        self.usuario_id = sessao.usuario_id if sessao is not None else usuario_id
        self.ao_sair = ao_sair
        self.ao_candidatar = ao_candidatar
        self.oportunidades_base = [
            Oportunidade("Aprendiz Administrativo", "Evolui Tecnologia", "Administrativo", "São Paulo", "Apoio às rotinas administrativas e atendimento.", "Ensino médio e boa comunicação.", oportunidade_id=1, salario="R$ 900,00", beneficios="Vale-transporte"),
            Oportunidade("Aprendiz de Atendimento", "Conecta Serviços", "Atendimento", "Campinas", "Atendimento ao público e organização de documentos.", "Vontade de aprender e organização.", oportunidade_id=2, salario="R$ 850,00", beneficios="Vale-transporte e refeição"),
            Oportunidade("Aprendiz de Tecnologia", "Núcleo Digital", "Tecnologia", "São Paulo", "Apoio ao time de suporte e testes de sistemas.", "Interesse por tecnologia.", oportunidade_id=3, salario="R$ 1.000,00", beneficios="Curso de capacitação")
        ]
        self.oportunidades = []
        self.candidaturas = []
        self.selecionada_id = None
        self.tela = tk.Toplevel(janela)
        self.tela.title("Oportunidades - Evolui")
        self.tela.geometry("980x680")
        self.criar_interface()
        self.carregar()

    def criar_interface(self):
        cabecalho = tk.Frame(self.tela)
        cabecalho.pack(fill="x", padx=20, pady=(15, 5))
        tk.Label(cabecalho, text="EVOLUI", font=("Arial", 20, "bold")).pack(side="left")
        tk.Button(cabecalho, text="Meu perfil", command=self.abrir_perfil).pack(side="right", padx=3)
        tk.Button(cabecalho, text="Minhas candidaturas", command=self.abrir_candidaturas).pack(side="right", padx=3)
        tk.Button(cabecalho, text="Sair", command=self.sair).pack(side="right", padx=3)
        tk.Label(self.tela, text="Oportunidades de Jovem Aprendiz", font=("Arial", 20, "bold")).pack(pady=8)
        barra = tk.Frame(self.tela)
        barra.pack(fill="x", padx=20)
        tk.Label(barra, text="Pesquisar:").pack(side="left")
        self.busca = tk.Entry(barra, width=40)
        self.busca.pack(side="left", padx=8)
        tk.Label(barra, text="Cidade:").pack(side="left")
        self.cidade = tk.Entry(barra, width=18)
        self.cidade.pack(side="left", padx=5)
        tk.Label(barra, text="Área:").pack(side="left")
        self.area = tk.Entry(barra, width=18)
        self.area.pack(side="left", padx=5)
        tk.Label(barra, text="Tipo:").pack(side="left")
        self.tipo = ttk.Combobox(barra, values=("Todos", "Jovem Aprendiz"), state="readonly", width=17)
        self.tipo.set("Jovem Aprendiz")
        self.tipo.pack(side="left", padx=5)
        tk.Button(barra, text="Pesquisar", command=self.carregar).pack(side="left", padx=5)

        self.lista = tk.Frame(self.tela)
        self.lista.pack(fill="both", expand=True, padx=20, pady=15)

    def carregar(self):
        termo = self.busca.get().strip().lower()
        cidade = self.cidade.get().strip().lower()
        area = self.area.get().strip().lower()
        self.oportunidades = [
            oportunidade for oportunidade in self.oportunidades_base
            if (not termo or termo in oportunidade.titulo.lower() or termo in oportunidade.empresa.lower() or termo in oportunidade.cidade.lower())
            and (not cidade or cidade in oportunidade.cidade.lower())
            and (not area or area in oportunidade.area.lower())
        ]
        for item in self.lista.winfo_children():
            item.destroy()
        for oportunidade in self.oportunidades:
            self.criar_card(oportunidade)
        if not self.oportunidades:
            tk.Label(self.lista, text="Nenhuma oportunidade encontrada.").pack(pady=30)

    def criar_card(self, oportunidade):
        card = tk.Frame(self.lista, relief="groove", borderwidth=1, padx=14, pady=10)
        card.pack(fill="x", pady=6)
        texto = tk.Frame(card)
        texto.pack(side="left", fill="x", expand=True)
        tk.Label(texto, text=oportunidade.titulo, font=("Arial", 13, "bold"), anchor="w").pack(fill="x")
        tk.Label(texto, text=f"{oportunidade.empresa} | {oportunidade.cidade} | {oportunidade.area}", anchor="w").pack(fill="x")
        tk.Label(texto, text=oportunidade.descricao, anchor="w", justify="left", wraplength=620).pack(fill="x", pady=3)
        tk.Button(card, text="Ver vaga", command=lambda: self.detalhes(oportunidade)).pack(side="right", padx=5)

    def selecionada(self):
        if self.selecionada_id is None:
            messagebox.showwarning("Atenção", "Selecione uma oportunidade.")
            return None
        return next(o for o in self.oportunidades if o.id == self.selecionada_id)

    def detalhes(self, oportunidade=None):
        if oportunidade is None:
            oportunidade = self.selecionada()
        if oportunidade is None:
            return
        self.selecionada_id = oportunidade.id
        detalhes = tk.Toplevel(self.tela)
        detalhes.title("Detalhes da oportunidade")
        detalhes.geometry("560x420")
        tk.Label(detalhes, text=oportunidade.titulo, font=("Arial", 18, "bold")).pack(pady=15)
        tk.Label(detalhes, text=f"Empresa: {oportunidade.empresa}\nCidade: {oportunidade.cidade}\nÁrea: {oportunidade.area}\nVagas: {oportunidade.quantidade_vagas}\nSalário: {oportunidade.salario or 'Não informado'}\nBenefícios: {oportunidade.beneficios or 'Não informado'}", justify="left").pack(anchor="w", padx=25)
        tk.Label(detalhes, text=f"Descrição:\n{oportunidade.descricao}\n\nRequisitos:\n{oportunidade.requisitos}", justify="left", wraplength=500, anchor="w").pack(anchor="w", padx=25, pady=15)
        tk.Button(detalhes, text="Candidatar-se", command=lambda: self.candidatar(oportunidade), width=20).pack(pady=10)

    def candidatar(self, oportunidade=None):
        oportunidade = oportunidade or self.selecionada()
        if oportunidade is None:
            return
        if self.usuario_id is None:
            messagebox.showwarning("Login necessário", "Entre como jovem para se candidatar.")
            return
        if oportunidade.id in self.candidaturas:
            messagebox.showinfo("Aviso", "Você já se candidatou a esta vaga.")
            return
        self.candidaturas.append(oportunidade.id)
        if self.ao_candidatar is not None:
            self.ao_candidatar(oportunidade)
        messagebox.showinfo("Sucesso", "Candidatura realizada com sucesso!")

    def abrir_perfil(self):
        if self.usuario_id is None:
            messagebox.showwarning("Login necessário", "Entre como jovem para acessar seu perfil.")
            return
        from views.tela_jovem import PerfilJovem

        PerfilJovem(self.tela, self.usuario_id, lambda: None)

    def sair(self):
        if self.ao_sair is not None:
            self.ao_sair()
        self.tela.destroy()

    def abrir_candidaturas(self):
        if self.usuario_id is None:
            messagebox.showwarning("Login necessário", "Entre como jovem para consultar candidaturas.")
            return
        registros = [oportunidade for oportunidade in self.oportunidades_base if oportunidade.id in self.candidaturas]
        if not registros:
            messagebox.showinfo("Minhas candidaturas", "Você ainda não tem candidaturas.")
            return
        texto = "\n".join(
            f"{oportunidade.titulo} | {oportunidade.empresa} | Status: Realizada"
            for oportunidade in registros
        )
        messagebox.showinfo("Minhas candidaturas", texto)
