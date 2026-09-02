def conectar():
    import mysql.connector

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="evolui"
    )

    return conexao