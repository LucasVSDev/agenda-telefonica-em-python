# Importando csv
import csv

######################### Função adicionar ####################################
def adicionar_dados(i):
    #Acessado cvs
    with open("dados/dados.csv", '+a', newline='') as file:
        escrever = csv.writer(file)
        escrever.writerow(i)

######################## Função ver dados #####################################
def ver_dados():
    dados = []
    #Acessado cvs
    with open("dados/dados.csv", 'r', newline='') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            dados.append(linha)
        return dados

#################### Função remover dados #####################################
def remover_dados(i):
    def adiciona_novalista(j):
        #Acessado cvs
        with open("dados/dados.csv", 'w', newline='') as file:
            escrever = csv.writer(file)
            escrever.writerows(j)
            ver_dados()

    
    nova_lista = []
    telefone = i
    with open("dados/dados.csv", 'r') as file:
        ler_csv = csv.reader(file)
        
        for linha in ler_csv:
            nova_lista.append(linha)
            for campo in linha:
                if campo == telefone:
                    nova_lista.remove(linha)
    
    # Adicionado nova lista
    adiciona_novalista(nova_lista)
    
#################### Função atualizar dados ###################################
def atualizar_dados(i):
    def adiciona_novalista(j):
        #Acessado cvs
        with open("dados/dados.csv", 'w', newline='') as file:
            escrever = csv.writer(file)
            escrever.writerows(j)
            ver_dados()

    nova_lista = []
    telefone = i[0]
    with open("dados/dados.csv", 'r') as file:
        ler_csv = csv.reader(file)
        
        for linha in ler_csv:
            nova_lista.append(linha)
            for campo in linha:
                if campo == telefone:
                    nome = i[1]
                    sexo = i[2]
                    tel = i[3]
                    email = i[4]
                    
                    dados = [nome, sexo, tel, email]
                    
                    # Trocando lista por index
                    index = nova_lista.index(linha)
                    nova_lista[index] = dados
    
    # Adicionado nova lista
    adiciona_novalista(nova_lista)

######################## Função pesquisar dados ###############################
def pesquisar_dados(i):
    dados = []
    telefone = i
    
    #Acessado cvs
    with open("dados/dados.csv", 'r') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            for campo in linha:
                if campo == telefone:
                    dados.append(linha)
    return dados

