import tkinter as tk
from tkinter import messagebox
from models import produto

def construir_aba_produto(pai, cursor, conn):
    frame = tk.Frame(pai)

    tk.Label(frame, text="Nome").grid(row=0, column=0)
    tk.Label(frame, text="Descrição").grid(row=1, column=0)
    tk.Label(frame, text="Preço").grid(row=2, column=0)
    tk.Label(frame, text="Estoque").grid(row=3, column=0)
    tk.Label(frame, text="Categoria ID").grid(row=4, column=0)

    nome = tk.Entry(frame)
    descricao = tk.Entry(frame)
    preco = tk.Entry(frame)
    estoque = tk.Entry(frame)
    categoria = tk.Entry(frame)

    nome.grid(row=0, column=1)
    descricao.grid(row=1, column=1)
    preco.grid(row=2, column=1)
    estoque.grid(row=3, column=1)
    categoria.grid(row=4, column=1)

    def salvar():
        try:
            produto.cadastrar_produto(cursor, conn, nome.get(), descricao.get(), float(preco.get()), int(estoque.get()), int(categoria.get()))
            messagebox.showinfo("Sucesso", "Produto cadastrado!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame, text="Cadastrar Produto", command=salvar).grid(row=5, column=0, columnspan=2)

    return frame
