class Oportunidade:

    def __init__(self, titulo, empresa, area, cidade, descricao, requisitos):
        self.titulo = titulo
        self.empresa = empresa
        self.area = area
        self.cidade = cidade
        self.descricao = descricao
        self.requisitos = requisitos

    def mostrar_oportunidade(self):
        print(self.titulo, "-", self.empresa)