# Importes #########################
from tkinter.ttk import *
from tkinter import *

from tkinter import messagebox

import sys
import csv

# Cores ######################
tema = "clam"
co0 = "#2e2d2d"  # Preta
co1 = "#E8E8E8"  # Cinza claro
co2 = "#CECECE"  # Cinza
co3 = "#38576b"  # Valor
co4 = "#403d3d"  # Letra
co5 = "#6f9fbd"  # Azul
co6 = "#ef5350"  # vermelha
co7 = "#93cd95"  # Verde


# Crinado janela#################
janela = Tk()
window_height = 450
window_width = 500

screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (screen_height / 3))

janela.title("")
janela.iconbitmap(r"img/agenda.ico")
janela.configure(background=co1)
janela.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use(tema)


#################### frames ############################
# Criando frames ------------------------------------------------
frameCima = Frame(janela, width=500, height=50, bg=co3, relief=FLAT)
frameCima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frameMeio = Frame(janela, width=500, height=150, bg=co1, padx=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=500, height=248, bg=co2, relief=FLAT)
frameBaixo.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky=NSEW)

janela.mainloop()