import tkinter as tk
from tkinter import messagebox, ttk

from models.empresa import Empresa


class TelaEmpresa:

    def __init__(self, janela, sessao=None, ao_sair=None):
        self.janela = janela
        self.sessao = sessao
        self.ao_sair = ao_sair
        self.empresa_id = 1
        self.vagas_exemplo = []
        self.candidatos_exemplo = []
        self.tela = tk.Toplevel(janela)
        self.tela.title("Área da Empresa - Evolui")
        self.tela.geometry("820x600")
        self.criar_interface()
        self.carregar_empresas()

    def criar_interface(self):
        tk.Label(self.tela, text="Área da Empresa", font=("Arial", 22, "bold")).pack(pady=14)
        self.resumo = tk.Label(self.tela, text="Empresa não cadastrada", anchor="w")
        self.resumo.pack(fill="x", padx=25)
        menu = tk.Frame(self.tela)
        menu.pack(pady=4)
        tk.Button(menu, text="Cadastrar Empresa", command=self.abrir_cadastro_empresa, width=19).pack(side="left", padx=3)
        tk.Button(menu, text="Cadastrar Oportunidade", command=self.abrir_cadastro_oportunidade, width=21).pack(side="left", padx=3)
        tk.Button(menu, text="Ver Oportunidades", command=self.abrir_oportunidades, width=18).pack(side="left", padx=3)
        tk.Button(menu, text="Ver Candidatos", command=self.abrir_candidatos, width=17).pack(side="left", padx=3)
        tk.Button(self.tela, text="Sair", command=self.sair, width=15).pack(pady=4)
        abas = ttk.Notebook(self.tela)
        abas.pack(fill="both", expand=True, padx=15, pady=8)
        cadastro = tk.Frame(abas)
        oportunidade = tk.Frame(abas)
        minhas_vagas = tk.Frame(abas)
        candidatos = tk.Frame(abas)
        self.abas = abas
        self.aba_cadastro = cadastro
        self.aba_oportunidade = oportunidade
        self.aba_minhas_vagas = minhas_vagas
        self.aba_candidatos = candidatos
        abas.add(cadastro, text="Dados da empresa")
        abas.add(oportunidade, text="Nova oportunidade")
        abas.add(minhas_vagas, text="Minhas vagas")
        abas.add(candidatos, text="Candidatos")
        self.criar_cadastro_empresa(cadastro)
        self.criar_cadastro_oportunidade(oportunidade)
        self.criar_minhas_vagas(minhas_vagas)
        self.criar_candidatos(candidatos)

    def criar_cadastro_empresa(self, frame):
        self.empresa_campos = {}
        for chave, rotulo in (("nome", "Nome da empresa"), ("cnpj", "CNPJ"), ("cidade", "Cidade"), ("email", "E-mail"), ("telefone", "Telefone")):
            tk.Label(frame, text=rotulo).pack(anchor="w", padx=30, pady=(12, 0))
            campo = tk.Entry(frame, width=55)
            campo.pack(padx=30)
            self.empresa_campos[chave] = campo
        tk.Button(frame, text="Salvar dados", command=self.salvar_empresa, width=20).pack(pady=20)

    def criar_cadastro_oportunidade(self, frame):
        self.oportunidade_campos = {}
        for chave, rotulo in (("titulo", "Cargo"), ("cidade", "Cidade"), ("quantidade_vagas", "Quantidade de vagas"), ("salario", "Salário"), ("beneficios", "Benefícios"), ("descricao", "Descrição"), ("requisitos", "Requisitos")):
            tk.Label(frame, text=rotulo).pack(anchor="w", padx=30, pady=(8, 0))
            campo = tk.Entry(frame, width=80)
            campo.pack(padx=30)
            self.oportunidade_campos[chave] = campo
        tk.Button(frame, text="Cadastrar oportunidade", command=self.salvar_oportunidade, width=25).pack(pady=18)

    def criar_candidatos(self, frame):
        self.candidatos_lista = ttk.Treeview(frame, columns=("nome", "cidade", "email", "vaga", "status"), show="headings")
        for coluna, titulo, largura in (("nome", "Nome", 180), ("cidade", "Cidade", 140), ("email", "E-mail", 220), ("vaga", "Oportunidade", 220), ("status", "Status", 110)):
            self.candidatos_lista.heading(coluna, text=titulo)
            self.candidatos_lista.column(coluna, width=largura)
        self.candidatos_lista.pack(fill="both", expand=True, padx=15, pady=15)
        tk.Button(frame, text="Atualizar candidatos", command=self.carregar_candidatos).pack(pady=8)

    def criar_minhas_vagas(self, frame):
        self.vagas_lista = ttk.Treeview(frame, columns=("cargo", "cidade", "vagas"), show="headings")
        for coluna, titulo, largura in (("cargo", "Cargo", 280), ("cidade", "Cidade", 180), ("vagas", "Vagas", 100)):
            self.vagas_lista.heading(coluna, text=titulo)
            self.vagas_lista.column(coluna, width=largura)
        self.vagas_lista.pack(fill="both", expand=True, padx=15, pady=15)
        self.vagas_lista.bind("<Double-1>", lambda evento: self.abrir_detalhes_vaga())
        tk.Button(frame, text="Ver detalhes e candidatos", command=self.abrir_detalhes_vaga, width=25).pack(pady=4)
        tk.Button(frame, text="Atualizar vagas", command=self.carregar_vagas).pack(pady=8)

    def carregar_empresas(self):
        dados = {
            "nome": "Empresa Exemplo",
            "cnpj": "00.000.000/0001-00",
            "cidade": "São Paulo",
            "email": "empresa@evolui.com",
            "telefone": "(11) 4000-0000"
        }
        for chave, campo in self.empresa_campos.items():
            campo.insert(0, dados[chave])
        self.resumo.config(text=f"Empresa: {dados['nome']}")
        self.carregar_vagas()

    def abrir_cadastro_empresa(self):
        self.abas.select(self.aba_cadastro)

    def abrir_cadastro_oportunidade(self):
        self.abas.select(self.aba_oportunidade)

    def abrir_oportunidades(self):
        self.abas.select(self.aba_minhas_vagas)
        self.carregar_vagas()

    def abrir_candidatos(self):
        self.abas.select(self.aba_candidatos)
        self.carregar_candidatos()

    def abrir_detalhes_vaga(self):
        selecao = self.vagas_lista.selection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione uma vaga para ver os detalhes.")
            return
        titulo, cidade, quantidade = self.vagas_lista.item(selecao[0], "values")
        dados = next((vaga for vaga in self.vagas_exemplo if vaga["titulo"] == titulo and vaga["cidade"] == cidade), {})
        detalhes = tk.Toplevel(self.tela)
        detalhes.title("Detalhes da vaga")
        detalhes.geometry("560x420")
        tk.Label(detalhes, text=titulo, font=("Arial", 18, "bold")).pack(pady=15)
        tk.Label(detalhes, text=f"Cidade: {cidade}\nVagas: {quantidade}\nSalário: {dados.get('salario') or 'Não informado'}\nBenefícios: {dados.get('beneficios') or 'Não informado'}", justify="left").pack(anchor="w", padx=25)
        tk.Label(detalhes, text=f"Descrição:\n{dados.get('descricao') or 'Não informado'}\n\nRequisitos:\n{dados.get('requisitos') or 'Não informado'}", justify="left", wraplength=500, anchor="w").pack(anchor="w", padx=25, pady=15)
        tk.Button(detalhes, text="Ver candidatos", command=self.abrir_candidatos, width=20).pack(pady=10)

    def salvar_empresa(self):
        valores = {chave: campo.get().strip() for chave, campo in self.empresa_campos.items()}
        if any(not valor for valor in valores.values()):
            messagebox.showwarning("Atenção", "Preencha todos os dados da empresa.")
            return
        empresa = Empresa(**valores, empresa_id=self.empresa_id)
        self.resumo.config(text=f"Empresa: {empresa.nome}")
        messagebox.showinfo("Sucesso", "Dados da empresa salvos!")

    def salvar_oportunidade(self):
        if not self.empresa_id:
            messagebox.showwarning("Atenção", "Salve os dados da empresa antes da oportunidade.")
            return
        valores = {chave: campo.get().strip() for chave, campo in self.oportunidade_campos.items()}
        if any(not valor for valor in valores.values()):
            messagebox.showwarning("Atenção", "Preencha todos os dados da oportunidade.")
            return
        try:
            quantidade = int(valores["quantidade_vagas"])
            if quantidade < 1:
                raise ValueError
            self.vagas_exemplo.append({**valores, "quantidade_vagas": quantidade})
            self.carregar_vagas()
            messagebox.showinfo("Sucesso", "Oportunidade cadastrada com sucesso!")
            for campo in self.oportunidade_campos.values():
                campo.delete(0, "end")
        except ValueError:
            messagebox.showwarning("Atenção", "A quantidade de vagas deve ser um número maior que zero.")

    def carregar_candidatos(self):
        for item in self.candidatos_lista.get_children():
            self.candidatos_lista.delete(item)
        for candidato in self.candidatos_exemplo:
            self.candidatos_lista.insert("", "end", values=candidato)

    def carregar_vagas(self):
        for item in self.vagas_lista.get_children():
            self.vagas_lista.delete(item)
        for vaga in self.vagas_exemplo:
            self.vagas_lista.insert("", "end", values=(vaga["titulo"], vaga["cidade"], vaga["quantidade_vagas"]))

    def sair(self):
        if self.ao_sair is not None:
            self.ao_sair()
        self.tela.destroy()
