import csv

arquivo = open("alunos.csv")
leia = csv.DictReader(arquivo)

for linha in leia:
    nota = float(linha["nota"])
    if nota >= 7:
        print(nota)