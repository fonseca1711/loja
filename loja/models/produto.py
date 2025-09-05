def criar_tabela_produto(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produto (
            id_produto SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            descricao TEXT,
            preco NUMERIC(10,2) CHECK (preco >= 0),
            estoque INT CHECK (estoque >= 0),
            id_categoria INT
        );
    """)

def cadastrar_produto(cursor, conn, nome, descricao, preco, estoque, id_categoria):
    cursor.execute("""
        INSERT INTO produto (nome, descricao, preco, estoque, id_categoria)
        VALUES (%s, %s, %s, %s, %s);
    """, (nome, descricao, preco, estoque, id_categoria))
    conn.commit()
