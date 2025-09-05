import tkinter as tk
from tkinter import messagebox
from models import item_pedido

def construir_aba_item(pai, cursor, conn):
    frame = tk.Frame(pai)

    tk.Label(frame, text="ID Pedido").grid(row=0, column=0)
    tk.Label(frame, text="ID Produto").grid(row=1, column=0)
    tk.Label(frame, text="Quantidade").grid(row=2, column=0)
    tk.Label(frame, text="Preço Unitário").grid(row=3, column=0)

    id_pedido = tk.Entry(frame)
    id_produto = tk.Entry(frame)
    quantidade = tk.Entry(frame)
    preco_unitario = tk.Entry(frame)

    id_pedido.grid(row=0, column=1)
    id_produto.grid(row=1, column=1)
    quantidade.grid(row=2, column=1)
    preco_unitario.grid(row=3, column=1)

    def salvar():
        try:
            item_pedido.cadastrar_item_pedido(cursor, conn, int(id_pedido.get()), int(id_produto.get()), int(quantidade.get()), float(preco_unitario.get()))
            messagebox.showinfo("Sucesso", "Item cadastrado e total do pedido atualizado!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame, text="Cadastrar Item", command=salvar).grid(row=4, column=0, columnspan=2)

    return frame
