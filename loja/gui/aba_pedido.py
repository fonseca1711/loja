import tkinter as tk
from tkinter import ttk, messagebox
from models import pedido, item_pedido

def construir_aba_pedido(pai, cursor, conn):
    frame = tk.Frame(pai)

    tk.Label(frame, text="ID Cliente").grid(row=0, column=0)
    tk.Label(frame, text="Valor Total").grid(row=1, column=0)
    tk.Label(frame, text="Status").grid(row=2, column=0)

    id_cliente = tk.Entry(frame)
    valor_total = tk.Entry(frame)
    status = tk.Entry(frame)

    id_cliente.grid(row=0, column=1)
    valor_total.grid(row=1, column=1)
    status.grid(row=2, column=1)

    def salvar():
        try:
            pedido.cadastrar_pedido(cursor, conn, int(id_cliente.get()), float(valor_total.get()), status.get())
            messagebox.showinfo("Sucesso", "Pedido cadastrado!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame, text="Cadastrar Pedido", command=salvar).grid(row=3, column=0, columnspan=2)

    # Visualização de itens
    tk.Label(frame, text="Ver itens do Pedido ID").grid(row=4, column=0)
    id_pedido = tk.Entry(frame)
    id_pedido.grid(row=4, column=1)

    tree = ttk.Treeview(frame, columns=("Produto", "Quantidade", "Preço"), show="headings")
    tree.heading("Produto", text="Produto")
    tree.heading("Quantidade", text="Quantidade")
    tree.heading("Preço", text="Preço Unitário")
    tree.grid(row=6, column=0, columnspan=2, sticky="nsew")

    def visualizar():
        try:
            itens = item_pedido.listar_itens_por_pedido(cursor, int(id_pedido.get()))
            for i in tree.get_children():
                tree.delete(i)
            for nome, qtd, preco in itens:
                tree.insert("", "end", values=(nome, qtd, f"R${preco:.2f}"))
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame, text="Ver Itens", command=visualizar).grid(row=5, column=0, columnspan=2)

    return frame
