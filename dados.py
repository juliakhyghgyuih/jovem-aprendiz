from conexao import conectar


class BancoEvolui:
    """Centraliza consultas do MVP e preserva as tabelas existentes."""

    def preparar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        try:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS empresas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    usuario_id INT NULL,
                    nome VARCHAR(150) NOT NULL,
                    cnpj VARCHAR(30) NOT NULL,
                    cidade VARCHAR(100) NOT NULL,
                    email VARCHAR(150) NOT NULL,
                    telefone VARCHAR(30) NOT NULL
                )
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS candidaturas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    usuario_id INT NOT NULL,
                    oportunidade_id INT NOT NULL,
                    status VARCHAR(30) NOT NULL DEFAULT 'Pendente',
                    data_candidatura DATETIME DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE KEY candidatura_unica (usuario_id, oportunidade_id)
                )
                """
            )
            self._adicionar_coluna(cursor, "perfis", "telefone", "VARCHAR(30) DEFAULT ''")
            self._adicionar_coluna(cursor, "usuarios", "tipo", "VARCHAR(20) NOT NULL DEFAULT 'jovem'")
            self._adicionar_coluna(cursor, "oportunidades", "quantidade_vagas", "INT DEFAULT 1")
            self._adicionar_coluna(cursor, "oportunidades", "empresa_id", "INT NULL")
            self._adicionar_coluna(cursor, "oportunidades", "salario", "VARCHAR(100) DEFAULT ''")
            self._adicionar_coluna(cursor, "oportunidades", "beneficios", "TEXT")
            self._adicionar_coluna(cursor, "empresas", "usuario_id", "INT NULL")
            self._adicionar_coluna(cursor, "candidaturas", "status", "VARCHAR(30) NOT NULL DEFAULT 'Pendente'")
            conexao.commit()
        finally:
            cursor.close()
            conexao.close()

    @staticmethod
    def _adicionar_coluna(cursor, tabela, coluna, definicao):
        cursor.execute(f"SHOW COLUMNS FROM {tabela} LIKE %s", (coluna,))
        if cursor.fetchone() is None:
            cursor.execute(f"ALTER TABLE {tabela} ADD COLUMN {coluna} {definicao}")

    def executar(self, sql, valores=(), muitos=False):
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        try:
            if muitos:
                cursor.executemany(sql, valores)
            else:
                cursor.execute(sql, valores)
            resultado = cursor.fetchall() if cursor.with_rows else []
            conexao.commit()
            return resultado
        finally:
            cursor.close()
            conexao.close()

    def consultar(self, sql, valores=()):
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        try:
            cursor.execute(sql, valores)
            return cursor.fetchall()
        finally:
            cursor.close()
            conexao.close()

    def inserir(self, sql, valores=()):
        conexao = conectar()
        cursor = conexao.cursor()
        try:
            cursor.execute(sql, valores)
            conexao.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            conexao.close()
