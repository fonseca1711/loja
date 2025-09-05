import psycopg2

def conectar():
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="postgres",
            user="postgres",
            password="1"
        )
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        print(f"Erro na conexão: {e}")
        return None, None
