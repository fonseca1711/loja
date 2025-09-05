def criar_tabela_cliente(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cliente (
            id_cliente SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            cpf VARCHAR(14) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            telefone VARCHAR(20),
            data_cadastro DATE DEFAULT CURRENT_DATE
        );
    """)

def cadastrar_cliente(cursor, conn, nome, cpf, email, telefone):
    cursor.execute("""
        INSERT INTO cliente (nome, cpf, email, telefone)
        VALUES (%s, %s, %s, %s);
    """, (nome, cpf, email, telefone))
    conn.commit()
