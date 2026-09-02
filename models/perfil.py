class Perfil:

    def __init__(self, idade, cidade, escolaridade, curso, habilidades):
        self.idade = idade
        self.cidade = cidade
        self.escolaridade = escolaridade
        self.curso = curso
        self.habilidades = habilidades

    def mostrar_perfil(self):
        print("Perfil de", self.cidade)