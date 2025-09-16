import csv

with open("py.csv", newline="", encoding="utf-8") as arquivo:
    leia = csv.DictReader(arquivo)

    for linha in leia:
        preco = int(linha["Preco"])  

        if preco <= 50000:
            print(linha)