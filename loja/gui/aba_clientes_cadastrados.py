import tkinter as tk
from tkinter import ttk, messagebox

def construir_aba_clientes_cadastrados(pai, cursor):
    frame = tk.Frame(pai)

    tree = ttk.Treeview(frame, columns=("ID", "Nome", "CPF", "Email", "Telefone"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("CPF", text="CPF")
    tree.heading("Email", text="Email")
    tree.heading("Telefone", text="Telefone")
    tree.pack(fill="both", expand=True)

    try:
        cursor.execute("SELECT id_cliente, nome, cpf, email, telefone FROM cliente;")
        for id_cliente, nome, cpf, email, telefone in cursor.fetchall():
            tree.insert("", "end", values=(id_cliente, nome, cpf, email, telefone))
    except Exception as e:
        messagebox.showerror("Erro ao carregar clientes", str(e))

    return frame
