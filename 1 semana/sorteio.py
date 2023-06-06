import random

aluno1 = input("Insira o nome do aluno 1: ")
aluno2 = input("Insira o nome do aluno 2: ")
aluno3 = input("Insira o nome do aluno 3: ")

lista = [aluno1, aluno2, aluno3]
sorteio = random.choice(lista)

print("O aluno sorteado foi: ", sorteio)