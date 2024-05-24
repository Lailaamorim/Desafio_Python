#Um professor quer sortear um dos  seus quatro alunos para apagar o quatro. faça um programa que ajude ele, 
#lendo os nomes dos alunos e escrevendo o nome do escolhido:
import random
n1 = (input("Primeiro nome: "))
n2 = (input("Segundo nome: "))
n3 = (input("Terceiro nome: "))
n4 = (input("Quarto nome: "))

lista = [n1, n2, n3, n4]
escolhido= random.choice(lista)
print (f"O aluno escolhido(a) foi: {escolhido}")