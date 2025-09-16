import os
os.mkdir("Projetos")
print("Pasta criada!")

open("Projrtos/matematica.")
open("Projrtos/ciencias.")
open("Projrtos/portugues.")
arquivo = os.listdir("projetos")

for item in arquivo:
    print(item)
os.rename("Projetos/relatorio_1.txt", "Projeto/historia.txt")


if os.path.exists("historia.txt"):
    os.remove("historia.txt")
    print("Arquivo apagado")
else:
    print("Arquivo não encontrado")