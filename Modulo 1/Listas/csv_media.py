
import csv

nota = []
arquivo = open("alunos.csv","r", newline="")
leia = csv.DictReader(arquivo)

for linha in leia:
    nota.append(float(linha["nota"]))

    media = sum(nota) / len(nota)
    print("A Média da turma é",round(media, 2))