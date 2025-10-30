### Automação do GitHub - Repositório Base __ POR ALUNO
## BIBLIOTECAS QUE VAMOS UTILIZAR: FLET, PYAUTOGUI,CSV OU JSON(banco de dados)
# 1 - CONTA DO GITHUB
# 2 - LINK DO REPOSITÓRIO BASE
# 3 - QUAL PASTA DO REPOSITORIO BASE IREMOS UTILIZAR... ( MODULO1, MODULO2, MODULO3...)
# 4 - QUAL SUB PASTA DESEJADA... DOS MÓDULOS EX...(CODIGOS BASE ETC...)
# 5 - CAMINHO DO SEU CÓDIGO ( MAQUINA PARA SUBIR NO GITHUB)

import flet as ft
import pyautogui as git
import sqlite3 as sq

lista_modulos = ['Modulo 1','Modulo 2','Modulo 3']
lista_repositorios_1 = ['Codigos Basicos','Condicionais','Exercicios','Extra','Listas','Loopings']
lista_repositorios_2 = ['APIs','Banco de Dados','Desenvolvimento Web','Exercicios','Extra','Manipulação de Arquivos e Automação...']
lista_repositorios_3 = ['']

def main(page: ft.Page):
    page.theme_mode = "dark"
    
    page.window.width = 800
    page.window.height = 600
    page.window.max_height = 600
    page.window.min_height = 600
    page.window.max_width = 800
    page.window.min_width = 800
    # git.mouseInfo()


    def logar(e):
        email_digitado = email.value
        senha_digitada = senha.value
         
        if senha.value != "" and email.value != "":
            try:
                git.press('Win')
                git.write("google")
                git.press('Enter')
                git.sleep(2)
                git.click(550,852)
                git.sleep(2)
                git.click(887,37)
                git.sleep(2)
                git.click(887,37)
                git.write("https://github.com/login",interval=0.1)
                git.press('Enter')
                git.sleep(2)
                git.write(f"{email_digitado}")
                git.press('Tab')
                git.sleep(2)
                git.write(f"{senha_digitada}")
                git.press('Enter')
                git.click(953,417)
                git.sleep(2)
                git.hotkey("Alt","Tab") 
            except:
                 page.open(ft.SnackBar(ft.Text("Nao cadastrado !",size=20,color="WHITE"),bgcolor="RED"))
                 page.update()
            botao_repositorio.visible = True
            modulos.visible = True
            pastas.visible = True
            email.visible= False
            senha.visible = False
            botao_iniciar.visible = False
            Enviar_Para_Modulo_Repositorio.visible = True
            botao_repositorio.visible = False
            page.update()
        else:
            page.open(ft.SnackBar(ft.Text("Nao cadastrado !",size=20,color="WHITE"),bgcolor="RED"))
            page.update()



    def Escolha_modulo(e):
        git.alert(text='Ok, iremos prosseguir', title='inserindo no modulo', button='OK')
        git.sleep(4)
        git.hotkey("Alt","Tab") 
        git.press('Enter')
        ##TROCAR  {REPOSITORIO BASE}  BANCO DE DADOS
        link = f"https://github.com/{email.value}/Repositorio_Base_Andrey"
        git.sleep(2) 
        git.click(699,60)
        git.write(link,interval=0.1)
        git.press('enter')
        page.update()
        page.open(ft.SnackBar(ft.Text("ESCOLHA O MODULO E REPOSITORIO",size=20,color="WHITE"),bgcolor="RED"))
        page.update()   
        if modulos.value == "Modulo 1":
                git.click(50,467)
                git.sleep(1)
                git.click(133,665)
                git.sleep(3)
                git.click(408,505)
                git.sleep(3)
                if pastas == "Codigos Basicos":
                    git.moveTo(421,474,duration=2)
                    git.click()
                elif pastas == "Condicionais":
                    git.moveTo(412,514,duration=2)
                    git.click()
                elif pastas == "Exercicios":
                    git.moveTo(404,553,duration=2)
                    git.click()
                elif pastas == "Extra":
                    git.moveTo(397,597,duration=2)
                    git.click()
                elif pastas == "Listas":
                    git.moveTo(399,636,duration=2)
                    git.click()
                elif pastas == "Loopings":
                    git.moveTo(406,677,duration=2)
                    git.click()
                else:
                    print("😁")
            
        elif modulos.value == "Modolo 2":
                git.click(50,467)
                git.sleep(1)
                git.click(133,665)
                git.sleep(3)
                git.click(408,547)
                git.sleep(3)
                if pastas == "":
                    git.moveTo(3,duration=2)
                    git.click()
                elif pastas == "":
                    git.moveTo(3,duration=2)
                    git.click()
                elif pastas == "":
                    git.moveTo(3,duration=2)
                    git.click()
                elif pastas == "":
                    git.moveTo(3,duration=2)
                    git.click()
                elif pastas == "":
                    git.moveTo(3,duration=2)
                    git.click()
                elif pastas == "":
                    git.moveTo(3,duration=2)
                    git.click()
                else:
                    print("👎🙄")
        elif modulos.value == "Modulo 3":
                git.click(50,467)
                git.sleep(1)
                git.click(133,665)
                git.sleep(3)
                git.click(408,587)
                git.sleep(3)
    page.update()   
    def on_repositorio_change(e):

        modulo_selecionado = modulos.value
        if modulo_selecionado == "Modulo 1":
            pastas.value = None
        
            pastas.options = [
                ft.dropdown.Option("Codigos"),
                ft.dropdown.Option("Basicos"),
                ft.dropdown.Option("Condicionais"),
                ft.dropdown.Option("Exercicios"),
                ft.dropdown.Option("Extra"),
                ft.dropdown.Option("Listas"),
                ft.dropdown.Option("Loopings"),
            ]
        elif modulo_selecionado == "Modulo 2":
            pastas.options = [
                ft.dropdown.Option("APIs"),
                ft.dropdown.Option("Banco de Dados"),
                ft.dropdown.Option("Desenvolvimento Web"),
                ft.dropdown.Option("Exercicios"),
                ft.dropdown.Option("Extra"),
                ft.dropdown.Option("Manipulação de Arquivos e Automação..."),
            ]
        elif modulo_selecionado == "Modulo 3":
            pastas.options = [
                ft.dropdown.Option("..."),
                ft.dropdown.Option("..."),
                ft.dropdown.Option("..."),
                ft.dropdown.Option("..."),
            ]
        pastas.visible = True
        page.update() 

        # def subir_No_GitHub():
        #     ...

    titulo = ft.Text("RPA de GitHub",size=40,color="white",font_family="Arial")
    email = ft.TextField(label="Digite seu email",width=300)
    senha = ft.TextField(label="Digite sua senha",width=300,password=True,can_reveal_password=True)
    botao_iniciar = ft.ElevatedButton("Logar no Git",on_click=logar,bgcolor="GREEN",width=300,color="black")
    # nao_login_bto = ft.ElevatedButton(text="Não Logar", on_click=lambda e: page.add(nao_logar()))
    botao_repositorio = ft.ElevatedButton("repositorio",on_click=Escolha_modulo,visible=False)
    modulos = ft.Dropdown(label="Qual o Modulo",width=300,options=[ft.dropdown.Option("Modulo 1"),
            ft.dropdown.Option("Modulo 2"),
            ft.dropdown.Option("Modulo 3")],on_change=on_repositorio_change,visible=False )
    pastas = ft.Dropdown(label="Escolha a pasta:",width=300,options=[],visible=False)
    Enviar_Para_Modulo_Repositorio = ft.ElevatedButton("Enviar Para O GitHub",on_click=Escolha_modulo,bgcolor="cyan",width=300,color="black",visible=False)



    page.add(
        ft.Row([titulo],alignment="center"),
        ft.Divider(height=10),
        ft.Row([email],alignment="center"),
        ft.Row([senha],alignment="center"),
        ft.Row([Enviar_Para_Modulo_Repositorio],alignment="center"),
        ft.Divider(height=10),
        ft.Row([modulos,pastas],alignment="center"),
        ft.Row([botao_iniciar,botao_repositorio],alignment="center"))




ft.app(target=main)
