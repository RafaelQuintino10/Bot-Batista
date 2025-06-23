import sqlite3

# Conecta (ou cria) o banco de dados chamado "exemplo.db"
conn = sqlite3.connect("grupos.db")

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# Cria a tabela "pessoas" com a nova coluna "data_vencimento"
cursor.execute("""
CREATE TABLE IF NOT EXISTS grupos_sinais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    chat_id NUMERIC

)
""")

# # Insere uma pessoa na tabela com data de vencimento
# cursor.execute(
#     "INSERT INTO pessoas (nome, idade, data_vencimento) VALUES (?, ?, ?)",
#     ("Alice", 30, "2025-07-01")
# )

# # Salva as alterações
# conn.commit()

# # Consulta todos os dados da tabela
# cursor.execute("SELECT * FROM pessoas")
# pessoas = cursor.fetchall()

# # Exibe os resultados
# for pessoa in pessoas:
#     print(pessoa)

# # Fecha a conexão com o banco de dados
# conn.close()
