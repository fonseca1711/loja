import tkinter as tk
from tkinter import messagebox
from models import cliente

def construir_aba_cliente(pai, cursor, conn):
    frame = tk.Frame(pai)

    tk.Label(frame, text="Nome").grid(row=0, column=0)
    tk.Label(frame, text="CPF").grid(row=1, column=0)
    tk.Label(frame, text="Email").grid(row=2, column=0)
    tk.Label(frame, text="Telefone").grid(row=3, column=0)

    nome = tk.Entry(frame)
    cpf = tk.Entry(frame)
    email = tk.Entry(frame)
    telefone = tk.Entry(frame)

    nome.grid(row=0, column=1)
    cpf.grid(row=1, column=1)
    email.grid(row=2, column=1)
    telefone.grid(row=3, column=1)

    def salvar():
        try:
            cliente.cadastrar_cliente(cursor, conn, nome.get(), cpf.get(), email.get(), telefone.get())
            messagebox.showinfo("Sucesso", "Cliente cadastrado!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(frame, text="Cadastrar Cliente", command=salvar).grid(row=4, column=0, columnspan=2)

    return frame
