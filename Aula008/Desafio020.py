# O mesmo professor  do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
# faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# Importa o módulo random, que contém funções para geração de números aleatórios
import random

# Solicita ao usuário que insira os nomes dos quatro alunos e os armazena em uma lista
alunos = []
for i in range(4):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    alunos.append(nome)

# Embaralha a ordem dos nomes na lista
random.shuffle(alunos)

# Exibe a ordem sorteada de apresentação dos trabalhos
print("A ordem de apresentação dos trabalhos é:")
for i, aluno in enumerate(alunos, start=1):
    print(f"{i}. {aluno}")
