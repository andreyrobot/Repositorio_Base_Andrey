def jogo():

    nome = input("digite seu nome: ")
    idade = int(input(f"Quantos anos o usuario {nome} tem?: "))

    if idade <= 18:
        print(f"{nome} é menor de idade")
    else:
        print(f"{nome} é maior de idade")

    topa =input(f"{nome} topa jogar comigo? você não tem escolha. pedra papel ou tesoura?:")

    if topa == "papel":
        print("tesoura, ganhei kk")
    elif topa == "tesoura":
        print("pedra, ganhei kk")
    elif topa == "pedra":
        print("papel, ganhei kk")
    else:
        print("oxi ta doido é?")

    jogo()

