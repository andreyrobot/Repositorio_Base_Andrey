# lista de mercado
lista = []
while True:
    compras = int(input("O que deseja Comprar: \n\n 1- Adicionar produto📥 \n 2- Ver Produtos Comprados👁️🗃️ \n 3- Modificar Produto↔🔂 \n 4- Remova Algum Produto \n 0- Sair\n"))
    if compras == 1:
        Produto = input("Qual Produto Deseja inserir?: \n\n")
        lista.append(Produto)
        print(f"\n Produto adicionado com Sucesso ! ➕{Produto}:\n\n")
    elif compras == 2:
        print(lista)
    elif compras == 3:
        Modificar = input("Modifique o Produto que deseja (●'◡'●): \n\n")
        if Modificar in lista:
            novo = input("Qual o Produto Novo?: \n")
            index = lista.index(Modificar)
            lista[index] = novo
            print(f"Sua Lista Foi Atualizada🆕...:\n")
            print(lista)
        else:
            print("item não encontrado")
    elif compras == 4:
        Produto = input("Digite o Produto Que deseja Remover: \n\n ")
        if Produto in lista:
            lista.remove(Produto)
            print(f"Seu item Foi Removido Com Sucesso❎")
            print(lista)
        else:
            print("item não encontrado")
    elif compras == 0:
        print("Saindo do programa.")
        break