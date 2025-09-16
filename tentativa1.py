def exibir_catalogo():
    print("\nCatálogo de Jogos:")
    for jogo, dados in catalogo.items():
        print(f"- {jogo}: R${dados['preco']:.2f}")

def processar_compra(jogo, quantidade):
    if jogo in catalogo:
        if quantidade > 0:
            if jogo in carrinho:
                carrinho[jogo] += quantidade
            else:
                carrinho[jogo] = quantidade
            print(f"{quantidade}x {jogo} adicionados ao carrinho.")
        else:
            print("Quantidade inválida.")
    else:
        print("Jogo não encontrado.")

def exibir_carrinho():
    total = 0
    if not carrinho:
        print("Carrinho vazio.")
    else:
        print("\nCarrinho de compras:")
        for jogo, quantidade in carrinho.items():
            preco_total_jogo = catalogo[jogo]['preco'] * quantidade
            total += preco_total_jogo
            print(f"- {jogo}: {quantidade} x R${catalogo[jogo]['preco']:.2f} = R${preco_total_jogo:.2f}")
        print(f"Total: R${total:.2f}")
    return total

def finalizar_compra():
    total = exibir_carrinho()
    if total > 0:
        print("Compra finalizada com sucesso!")
        carrinho.clear()
    else:
        print("Carrinho vazio. Nada para finalizar.")


catalogo = {
    "Jogo A": {"preco": 50.00},
    "Jogo B": {"preco": 75.00},
    "Jogo C": {"preco": 100.00}
}
carrinho = {}

while True:
    print("\nOpções:")
    print("1. Ver catálogo")
    print("2. Ver carrinho")
    print("3. Finalizar compra")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        exibir_catalogo()
    elif escolha == '2':
        exibir_carrinho()
    elif escolha == '3':
        finalizar_compra()
    elif escolha == '4':
        break
    else:
        print("Opção inválida.")

print("Obrigado por usar a loja de jogos!")