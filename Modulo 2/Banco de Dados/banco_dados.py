import sqlite3 as sq

# Alunos

# Autores

# Livros

# Empréstimos
banco = sq.connect('dados_de_Biblioteca.db')

                                    ##CREATES TABLESS:
cursor = banco.cursor()
                        #ALUNO
cursor.execute("CREATE TABLE IF NOT EXISTS Alunos (nome TEXT, Numero INTEGER,Turma TEXT, Media_de_notas REAL)")
                        ##AUTORES
cursor.execute("CREATE TABLE IF NOT EXISTS Autores (nome TEXT, Quanto_livros_criou INTEGER, Idade INTEGER)")
                        ###LIVROS
cursor.execute("CREATE TABLE IF NOT EXISTS Livros (nome TEXT, Quantas_copias INTEGER, Tema TEXT, Custo_Do_Livro REAL)")
                        ####EMPRESTIO
cursor.execute("CREATE TABLE IF NOT EXISTS Emprestimo (nome_banco TEXT, Quantos_Devem INTEGER, Maior_Devedor TEXT, MAXIMO_DE_EMPRESTIMO REAL)")


                                    ##INSERTSSS:

cursor.execute("INSERT INTO Alunos (nome, Numero, Turma, Media_de_notas) VALUES ('Yuri', 21, ' Ouro ',6.7)")

cursor.execute("INSERT INTO Autores (nome, Quanto_livros_criou, Idade) VALUES ('mauricio', 125, 34)")

cursor.execute("INSERT INTO Livros (nome, Quantas_copias, Tema, Custo_Do_Livro ) VALUES ('O protagonista Sem Olofotes', 506, 'Superação/Futbol', 45.6 )")

cursor.execute("INSERT INTO Emprestimo (nome_banco, Quantos_Devem, Maior_Devedor, MAXIMO_DE_EMPRESTIMO) VALUES ('madresco', 231, 'alex', 700000)")


# cursor.execute("UPDATE Alunos SET turma = Ouro WHERE turma = Esmeralda ")
# cursor.execute("DELETE FROM Alunos Where nome = 'Yuri' ")

banco.commit()


cursor.execute("SELECT * FROM Alunos")


print("=== Dados no banco ===")
for linha in cursor.fetchall():
    print(linha)


banco.close()
