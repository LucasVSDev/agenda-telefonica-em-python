# Importes #########################
from tkinter.ttk import *
from tkinter import ttk
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
co8 = "#FFFFFF"  # Branco

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

# #################### frames ############################
# Criando frames ------------------------------------------------
frameCima = Frame(janela, width=500, height=50, bg=co3, relief='flat')
frameCima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frameMeio = Frame(janela, width=500, height=150, bg=co1, relief="flat")
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=500, height=248, bg=co2, relief="flat")
frameBaixo.grid(row=2, column=0, columnspan=2, pady=1, padx=10, sticky=NW)

# # Configurando frames titulo cima --------------------------------------
l_titulo = Label(
    frameCima,
    text="Agenda Telefônica",
    anchor=NE,
    font=("roboto 20 bold"),
    bg=co3,
    fg=co1,
)
l_titulo.place(x=5, y=5)

l_linha = Label(
    frameCima, text="", width=500, anchor=NE, font=("roboto 1"), bg=co2, fg=co1
)
l_linha.place(x=0, y=46)

# Configurando Label esqundo meio --------------------------------------
l_nome = Label(
    frameMeio, text="Nome *", anchor=NW, font=("roboto 10 bold"), bg=co1, fg=co4
)
l_nome.place(x=10, y=20)
e_nome = Entry(frameMeio, width=25, justify=LEFT, relief=FLAT, font=("", 10), highlightthickness=1)
e_nome.place(x=80, y=20)

l_sexo = Label(
    frameMeio, text="Sexo *", anchor=NW, font=("roboto 10 bold"), bg=co1, fg=co4
)
l_sexo.place(x=10, y=50)
e_sexo = Combobox(frameMeio, width=27)
e_sexo["value"] = ("", "F", "M")
e_sexo.place(x=80, y=50)

l_tel = Label(
    frameMeio, text="Telefone *", anchor=NW, font=("roboto 10 bold"), bg=co1, fg=co4
)
l_tel.place(x=10, y=80)
e_tel = Entry(frameMeio, width=25, justify=LEFT, relief=FLAT, font=("", 10), highlightthickness=1)
e_tel.place(x=80, y=80)

l_email = Label(
    frameMeio, text="Email *", anchor=NW, font=("roboto 10 bold"), bg=co1, fg=co4
)
l_email.place(x=10, y=110)
e_email = Entry(frameMeio, width=25, justify=LEFT, relief=FLAT, font=("", 10), highlightthickness=1)
e_email.place(x=80, y=110)

# Configurando button direito meio --------------------------------------
b_procurar = Button(
    frameMeio,
    text="Procurar",
    font=("roboto 8 bold"),
    bg=co1,
    fg=co4,
    relief=RAISED,
    overrelief=RIDGE,
)
b_procurar.place(x=288, y=20)
e_procurar = Entry(
    frameMeio, width=16, justify=LEFT, relief=FLAT, font=("", 11), highlightthickness=1
)
e_procurar.place(x=347, y=21)

b_ver = Button(
    frameMeio,
    text="Ver dados",
    width=10,
    font=("arial 8 bold"),
    bg=co1,
    fg=co4,
    relief=RAISED,
    overrelief=RIDGE,
)
b_ver.place(x=288, y=50)

b_ver = Button(
    frameMeio,
    text="Adicionar",
    width=10,
    font=("arial 8 bold"),
    bg=co1,
    fg=co4,
    relief=RAISED,
    overrelief=RIDGE,
)
b_ver.place(x=400, y=50)

l_atualizar = Button(
    frameMeio,
    text="Atualizar",
    width=10,
    font=("arial 8 bold"),
    bg=co7,
    fg=co8,
    relief=RAISED,
    overrelief=RIDGE,
)
l_atualizar.place(x=400, y=80)

l_deletar = Button(
    frameMeio,
    text="Deletar",
    width=10,
    font=("arial 8 bold"),
    bg=co6,
    fg=co8,
    relief=RAISED,
    overrelief=RIDGE,
)
l_deletar.place(x=400, y=110)

# Configurando tabela baixo --------------------------------------

#crinado um treeview com uma scrollbar
cabecalho = ["Nome","Sexo","Telefone","Email"]
dados = ["Joao pesso", "M", "(91)987484562","joao@test.com"], ["Maria clara", "F", "(91)987596324","maria@test.com"]

global tree

tree = ttk.Treeview(frameBaixo, selectmode=EXTENDED, columns=cabecalho, show="headings")

vsb = ttk.Scrollbar(frameBaixo, orient=VERTICAL, command=tree.yview)

tree.configure(yscrollcommand=vsb.set)

tree.grid(column=0, row=0, sticky=NSEW)
vsb.grid(column=1, row=0, sticky=NS)

hd = ["nw","nw","nw","nw","nw"]
h = [120,50,80,120,200]
n = [0]

#tree cabeçalho
tree.heading(0, text="Nome", anchor=NW)
tree.heading(1, text="Sexo", anchor=NW)
tree.heading(2, text="Telefone", anchor=NW)
tree.heading(3, text="Email", anchor=NW)

# tree corpo
tree.column(0, width=120, anchor='nw')
tree.column(1, width=50, anchor='nw')
tree.column(2, width=100, anchor='nw')
tree.column(0, width=120, anchor=hd[0])

for item in dados:
    tree.insert('', "end", values=item)

janela.mainloop()
