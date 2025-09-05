def criar_tabela_item_pedido(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS item_pedido (
            id_item SERIAL PRIMARY KEY,
            id_pedido INT REFERENCES pedido(id_pedido),
            id_produto INT REFERENCES produto(id_produto),
            quantidade INT CHECK (quantidade > 0),
            preco_unitario NUMERIC(10,2) CHECK (preco_unitario >= 0)
        );
    """)

def cadastrar_item_pedido(cursor, conn, id_pedido, id_produto, quantidade, preco_unitario):
    cursor.execute("""
        INSERT INTO item_pedido (id_pedido, id_produto, quantidade, preco_unitario)
        VALUES (%s, %s, %s, %s);
    """, (id_pedido, id_produto, quantidade, preco_unitario))
    conn.commit()
    atualizar_total_pedido(cursor, conn, id_pedido)

def atualizar_total_pedido(cursor, conn, id_pedido):
    cursor.execute("""
        SELECT SUM(quantidade * preco_unitario)
        FROM item_pedido
        WHERE id_pedido = %s;
    """, (id_pedido,))
    total = cursor.fetchone()[0] or 0
    cursor.execute("""
        UPDATE pedido
        SET valor_total = %s
        WHERE id_pedido = %s;
    """, (total, id_pedido))
    conn.commit()

def listar_itens_por_pedido(cursor, id_pedido):
    cursor.execute("""
        SELECT p.nome, ip.quantidade, ip.preco_unitario
        FROM item_pedido ip
        JOIN produto p ON ip.id_produto = p.id_produto
        WHERE ip.id_pedido = %s;
    """, (id_pedido,))
    return cursor.fetchall()
