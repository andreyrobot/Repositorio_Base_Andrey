import csv

arquivo = open("alunos.csv")
leia = csv.DictReader(arquivo)

for linha in leia:
    print(linha["nome"])
