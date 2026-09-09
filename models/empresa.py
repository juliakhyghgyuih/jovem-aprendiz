class Empresa:

    def __init__(self, nome, cnpj, cidade, email, telefone, empresa_id=None):
        self.id = empresa_id
        self.nome = nome
        self.cnpj = cnpj
        self.cidade = cidade
        self.email = email
        self.telefone = telefone
