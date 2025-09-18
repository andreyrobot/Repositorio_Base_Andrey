### Automação do GitHub - Repositório Base __ POR ALUNO
## BIBLIOTECAS QUE VAMOS UTILIZAR: FLET, PYAUTOGUI,CSV OU JSON
# 1 - CONTA DO GITHUB
# 2 - LINK DO REPOSITÓRIO BASE
# 3 - QUAL PASTA DO REPOSITORIO BASE IREMOS UTILIZAR... ( MODULO1, MODULO2, MODULO3...)
# 4 - QUAL SUB PASTA DESEJADA... DOS MÓDULOS EX...(CODIGOS BASE ETC...)
# 5 - CAMINHO DO SEU CÓDIGO ( MAQUINA PARA SUBIR NO GITHUB)

import flet as ft
import pyautogui as git
import csv 
lista_modulos = ['Modulo 1','Modulo 2','Modulo 3']
lista_repositorios_1 = ['Codigos Basicos','Condicionais','Exercicios','Extra','Listas','Loopings']
lista_repositorios_2 = ['APIs','Banco de Dados','Desenvolvimento Web','Exercicios','Extra','Manipulação de Arquivos e Automação...']
lista_repositorios_3 = ['']

def main(page: ft.Page):

    # git.mouseInfo()


    def logar(e):
        email_digitado = email.value
        senha_digitada = senha.value
        try:
            git.press('Win')
            git.write("https://github.com/login",interval=0.1)
            git.press('Enter')
            git.sleep(2)
            git.write(f"{email_digitado}")
            git.press('Tab')
            git.write(f"{senha_digitada}")
        except:
            print("Algo De Errado Não Deu Certo❎")
    
    def carregar_no_repositorio(e):
        print("aqui vc coloca para subir no repositorio")

    email = ft.TextField(label="Digite seu email",width=200)
    senha = ft.TextField(label="Digite sua senha",width=200,password=True,can_reveal_password=True)
    botao_iniciar = ft.ElevatedButton("Logar no Git",on_click=logar)
    botao_repositorio = ft.ElevatedButton("repositorio",on_click=carregar_no_repositorio)
    modulos = ft.Dropdown(label="Escolha o Modulo",width=300,options=[ft.dropdown.Option("Modulo 1"),
            ft.dropdown.Option("Modulo 2"),
            ft.dropdown.Option("Modulo 3")])
    page.add(ft.Row([email],alignment="center"),
        ft.Row([senha,modulos],alignment="center"),
             ft.Row([botao_iniciar],alignment="center"),
             ft.Row([botao_repositorio],alignment="center"))
             
ft.app(target=main)




# https://github.com/andreyrobot/Repositorio_Base_Andrey
# https://github.com/andreyrobot/Repositorio_Base_Andrey/tree/main/Modulo%201

# Codigos Basicos
# Orientações.txt
# print.py
# Condicionais
# CS_V.py
# Fléte.py
# Orientações.txt
# alunos.csv
# cs_writ.py
# csv_+7.py
# csv_.py
# csv_media.py
# csvv.py
# ftt.csv
# Exercicios
# Orientações.txt
# Extra
# Conversor_de_Moedas.py
# Orientações.txt
# py.csv
# pygame1.py
# Listas
# CS_V.py
# Fléte.py
# Orientações.txt
# alunos.csv
# cs_writ.py
# csv_+7.py
# csv_.py
# csv_media.py
# csvv.py
# ftt.csv
# Loopings
# Orientações.txt
# Modulo 2
# APIs
# Banco de Dados
# Desenvolvimento Web
# Exercicios
# Extra
# Manipulação de Arquivos e Automação
# Modulo 3
# Em construção.txt
# README.md