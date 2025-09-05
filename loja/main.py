import tkinter as tk
from gui.interface import LojaGUI

def main():
    root = tk.Tk()
    app = LojaGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.fechar)
    root.mainloop()

if __name__ == "__main__":
    main()
