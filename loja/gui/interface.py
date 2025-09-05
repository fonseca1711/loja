import tkinter as tk
from tkinter import ttk
from db.conexao import conectar
from models import cliente, produto, pedido, item_pedido

# Importação das abas
from gui.aba_cliente import construir_aba_cliente
from gui.aba_produto import construir_aba_produto
from gui.aba_pedido import construir_aba_pedido
from gui.aba_item import construir_aba_item
from gui.aba_estoque import construir_aba_estoque
from gui.aba_clientes_cadastrados import construir_aba_clientes_cadastrados

class LojaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🛒 Loja Virtual")
        self.root.geometry("1000x650")
        self.conn, self.cursor = conectar()

        # Criação das tabelas
        cliente.criar_tabela_cliente(self.cursor)
        produto.criar_tabela_produto(self.cursor)
        pedido.criar_tabela_pedido(self.cursor)
        item_pedido.criar_tabela_item_pedido(self.cursor)
        self.conn.commit()

        self.criar_interface()

    def criar_interface(self):
        abas = ttk.Notebook(self.root)

        # Adiciona cada aba à interface
        abas.add(construir_aba_cliente(abas, self.cursor, self.conn), text="Cadastro de Clientes")
        abas.add(construir_aba_produto(abas, self.cursor, self.conn), text="Cadastro de Produtos")
        abas.add(construir_aba_pedido(abas, self.cursor, self.conn), text="Cadastro de Pedidos")
        abas.add(construir_aba_item(abas, self.cursor, self.conn), text="Itens do Pedido")
        abas.add(construir_aba_estoque(abas, self.cursor), text="Produtos Disponíveis")
        abas.add(construir_aba_clientes_cadastrados(abas, self.cursor), text="Clientes Cadastrados")

        abas.pack(expand=1, fill="both")

        # Botão para sair do programa
        tk.Button(self.root, text="🚪 Sair do Programa", command=self.fechar).pack(pady=10)

    def fechar(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        self.root.destroy()
