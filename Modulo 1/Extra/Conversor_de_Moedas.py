def inicio():
    print("Bem vindo ao Conversor de Moedas")
    print("Este app converte Dólar para Real e Real para Dólar")
    print("Apenas maiores de idade podem usar este app")
nome = input("Por favor Digite seu nome: ")
idade = int(input(f"ok Quantos anos {nome} tem?:"))

if idade < 18:
    exit()
else:
    print(f"ok {nome} vamos começar")

def Converter_Dolar_para_Real():
    print(f"Seu Saldo está em Real Sr {nome}")

def Converter_Real_para_Dolar():
    print(f"Seu Saldo está em Dólar Sr {nome}")

opção = 4
while opção !=3:
    opções = input("Digite a opção que deseja:/n1 - Conversão do Real para o Dolar/n2 - Conversão do Real para o Dolar /n3 Eu quero Sair do app")
    if opções == "1":
        valor = float(input("Digite o valor em Dólar que deseja converter para Real: "))
        valor_convertido = valor * 5.25
        print(f"O valor de {valor} Dólares é equivalente a {valor_convertido} Reais")
        Converter_Dolar_para_Real()
    elif opções == "2":
        valor = float(input("Digite o valor em Real que deseja converter para Dólar: "))
        valor_convertido = valor / 5.25
        print(f"O valor de {valor} Reais é equivalente a {valor_convertido} Dólares")
        Converter_Real_para_Dolar()
    elif opção == "3":
        print("Obrigado por usar o Conversor de Moedas")
        break
    else:
        print("Opção inválida, tente novamente")