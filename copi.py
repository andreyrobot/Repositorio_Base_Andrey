# lista jogos
nome = input("Digite seu nome: ")
print(f"Olá {nome}, bem-vindo à nossa loja de jogos!")
lista_de_jogos = ["Hollow_knithe", "Call Of Duty", "Celeste"]

print("Precisamos saber sua idade para continuar")
idade = int(input("Digite sua idade:"))
if idade < 18:
    lista_de_jogos = ["Hollow knithe", "Celeste"]
    print("Você não pode acessar todos os jogos, apenas os permitidos para menores de idade")
    print("OPÇOES ACESSEVEIS:")
    for jogo in lista_de_jogos:
        print(f"- {jogo}")
else:
    print("Você pode acessar todos os jogos")
    print(lista_de_jogos)
    print("OPÇOES ACESSEVEIS:")

# tentativa de fazer mais jogos

print("Deseja ver mais jogos?")
resposta = input("Digite 'sim' ou 'não': ").strip().lower()
if resposta == "sim":
    print("Aqui estão mais jogos disponíveis:")
    lista_de_jogos.append("The Witcher 3")
    lista_de_jogos.append("God of War")
    lista_de_jogos.append("Minecraft")
    lista_de_jogos.append("Final Fantasy VII Remake")

    def lista_de_compras():
        print("Lista de compras:")
        for jogo in lista_de_jogos:
            print(f"- {jogo}")

    lista_de_compras()
    print("Qual produto você deseja adicionar à lista?: ")
    produto = input("Digite o nome do produto: ")
    lista_de_jogos.append(produto)
    for jogo in lista_de_jogos:
        print(f"- {jogo}")
else:
    print("Ok, sem problemas!")

    def lista_de_compras():
        print("Lista de compras:")
        for jogo in lista_de_jogos:
            print(f"- {jogo}")

    lista_de_compras()
    print("Qual produto você deseja adicionar à lista?: ")
    produto = input("Digite o nome do produto: ")
    lista_de_jogos.append(produto)

    print("Mais algum produto que deseja adicionar?")
    resposta = input("Digite 'sim' ou 'não': ").strip().lower()
    if resposta == "sim":
        produto = input("Digite o nome do produto: ")
        lista_de_jogos.append(produto)
    else:
        print("Obrigado por visitar nossa loja de jogos!")
    for jogo in lista_de_jogos:
        print(f"- {jogo}")

        print(f"Sr {nome} esses foram os jogos que você escolheu:")
        for jogo in lista_de_jogos:
            print(f"- {jogo}")
        lista_de_jogos.remove(produto)
        print("Qual jogo você deseja remover da lista?")
        jogo_remover = input("Digite o nome do jogo a remover: ")
        if jogo_remover in lista_de_jogos:
            lista_de_jogos.remove(jogo_remover)
            print(f"O jogo {jogo_remover} foi removido da lista.")
        else:
            print(f"O jogo {jogo_remover} não está na lista.")