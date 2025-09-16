nome = input("Digite seu nome cidadão😁: ")
email = input(f"Poderia me Afirmar Seu {nome} e-mail: ")

arquivo = open ("pessoa.txt" , "a")
arquivo.write(nome + " | " + email + "/n")
arquivo.close