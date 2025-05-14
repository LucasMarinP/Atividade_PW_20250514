CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS categoria (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL
)
"""

INSERIR = """
INSERT INTO produto (id, nome,) 
VALUES (?, ?)
"""

OBTER_TODOS = """
SELECT 
id, nome, 
FROM produto
ORDER BY nome
""" 