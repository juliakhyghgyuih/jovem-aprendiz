class Sessao:
    """Mantem o usuario autenticado durante a execucao do aplicativo."""

    def __init__(self):
        self.usuario_id = None
        self.tipo = None
        self.nome = None
        self.email = None

    @property
    def autenticada(self):
        return self.usuario_id is not None and self.tipo in ("jovem", "empresa")

    def iniciar(self, usuario):
        self.usuario_id = usuario["id"]
        self.tipo = (usuario.get("tipo") or "jovem").strip().lower()
        self.nome = usuario.get("nome")
        self.email = usuario.get("email")

    def encerrar(self):
        self.usuario_id = None
        self.tipo = None
        self.nome = None
        self.email = None
