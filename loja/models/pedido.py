def criar_tabela_pedido(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedido (
            id_pedido SERIAL PRIMARY KEY,
            id_cliente INT,
            data_pedido DATE DEFAULT CURRENT_DATE,
            valor_total NUMERIC(10,2),
            status VARCHAR(50)
        );
    """)

def cadastrar_pedido(cursor, conn, id_cliente, valor_total, status):
    cursor.execute("""
        INSERT INTO pedido (id_cliente, valor_total, status)
        VALUES (%s, %s, %s);
    """, (id_cliente, valor_total, status))
    conn.commit()
