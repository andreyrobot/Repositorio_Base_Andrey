import os
import flet as ft

def interface(page: ft.Page):
    page.title = "interface cp do fessor😁👍"
    page.theme_mode = "dark"

    texto_pasta = ft.TextField(label="Nome da pasta")
    texto_arquivo = ft.TextField(label="Nome do arquivo")

    def criar_pasta(e):
        nome_pasta = texto_pasta.value
        if nome_pasta:
            try:
                os.mkdir(nome_pasta)
                page.snack_bar = ft.SnackBar(ft.Text(f"Pasta '{nome_pasta}' criada!"))
            except FileExistsError:
                page.snack_bar = ft.SnackBar(ft.Text("Pasta já existe!"))
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Digite o nome da pasta!"))
        page.snack_bar.open = True
        page.update()

    def criar_arquivo(e):
        nome_arquivo = texto_arquivo.value
        if nome_arquivo:
            with open(nome_arquivo, "w", encoding="utf-8") as f:
                f.write("")  # Cria arquivo vazio
            page.snack_bar = ft.SnackBar(ft.Text(f"Arquivo '{nome_arquivo}' criado!"))
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Digite o nome do arquivo!"))
        page.snack_bar.open = True
        page.update()

    botao_pasta = ft.ElevatedButton("CRIAR PASTA", bgcolor="PURPLE", color="WHITE", width=200, on_click=criar_pasta)
    botao_arquivo = ft.ElevatedButton("CRIAR ARQUIVO", bgcolor="RED", color="BLACK", width=200, on_click=criar_arquivo)

    page.add(
        ft.Row([texto_pasta], alignment="center"),
        ft.Row([botao_pasta], alignment="center"),
        ft.Row([texto_arquivo], alignment="center"),
        ft.Row([botao_arquivo], alignment="center"),
    )

ft.app(target=interface)