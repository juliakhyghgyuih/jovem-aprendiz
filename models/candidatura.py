class Candidatura:

    def __init__(self, usuario_id, oportunidade_id, candidatura_id=None):
        self.id = candidatura_id
        self.usuario_id = usuario_id
        self.oportunidade_id = oportunidade_id
