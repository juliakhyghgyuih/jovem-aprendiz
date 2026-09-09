class Oportunidade:

    def __init__(self, titulo, empresa, area, cidade, descricao, requisitos, quantidade_vagas=1, oportunidade_id=None, salario="", beneficios=""):
        self.id = oportunidade_id
        self.titulo = titulo
        self.empresa = empresa
        self.area = area
        self.cidade = cidade
        self.descricao = descricao
        self.requisitos = requisitos
        self.quantidade_vagas = quantidade_vagas
        self.salario = salario
        self.beneficios = beneficios

    def mostrar_oportunidade(self):
        print(self.titulo, "-", self.empresa)