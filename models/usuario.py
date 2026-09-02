class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def cadastrar(self):
        print("Usuário cadastrado:", self.nome)