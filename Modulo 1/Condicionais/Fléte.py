import flet as ft
import csv


def main(page:ft.Page):
    page.title = "Cadastro login"
    page.theme_mode = "Dark"

    def clique(e):
        valor_login = texto_login.value
        valor_senha = texto_senha.value
        
        with open("ftt.csv","a", newline="") as arquivo:
           escritor =  csv.writer(arquivo)
        escritor.writerow([valor_login,valor_senha])
    page.update()
    texto_login = ft.TextField(label="login", border_color="Red", focus_color="Green")
    texto_senha = ft.TextField(label="senha", password=True, can_reveal_password=True)

    botao = ft.ElevatedButton("Cadastro", on_click=clique)

    page.add(texto_login, texto_senha, botao)

ft.app(target=main)
