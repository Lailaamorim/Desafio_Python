#Um professor quer sortear um dos  seus quatro alunos para apagar o quatro. faça um programa que ajude ele, 
#lendo os nomes dos alunos e escrevendo o nome do escolhido:

# Importa o módulo random, que contém funções para geração de números aleatórios
import random
n1 = (input("Primeiro nome: "))
n2 = (input("Segundo nome: "))
n3 = (input("Terceiro nome: "))
n4 = (input("Quarto nome: "))
# Coloca os nomes em uma lista
lista = [n1, n2, n3, n4]
# Escolhe aleatoriamente um nome da lista usando a função random.choice
escolhido= random.choice(lista)
# Exibe o nome escolhido aleatoriamente
print (f"O aluno escolhido(a) foi: {escolhido}")