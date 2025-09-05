import tkinter as tk
from tkinter import ttk, messagebox

def construir_aba_estoque(pai, cursor):
    frame = tk.Frame(pai)

    tree = ttk.Treeview(frame, columns=("Nome", "Preço", "Estoque", "Categoria"), show="headings")
    tree.heading("Nome", text="Nome")
    tree.heading("Preço", text="Preço")
    tree.heading("Estoque", text="Estoque")
    tree.heading("Categoria", text="Categoria")
    tree.pack(fill="both", expand=True)

    try:
        cursor.execute("""
            SELECT p.nome, p.preco, p.estoque, c.nome
            FROM produto p
            LEFT JOIN categoria c ON p.id_categoria = c.id_categoria;
        """)
        for nome, preco, estoque, categoria in cursor.fetchall():
            tree.insert("", "end", values=(nome, f"R${preco:.2f}", estoque, categoria or "Sem categoria"))
    except Exception as e:
        messagebox.showerror("Erro ao carregar produtos", str(e))

    return frame
