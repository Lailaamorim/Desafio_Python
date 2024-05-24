#faça um programa que leia o nome completo de uma pessoa, 
#mostrando em seguida o primeiro e o último nome separadamente.

#ex: Ana Maria de Souza
#Primeiro: Anna
#Segundo : Souza

nome = input("Digite seu nome completo: ").strip().upper()
nome = nome.split()
print("Muito prazer em te conhecer! ")
print(f"Seu primeiro nome é: {(nome[0])}")#Esse nome[0] diz para ele pegar a palavra que está fatiada na 
#primeira posição ou seja o primeiro nome
print(f"Seu último nome é {(nome[len(nome)-1])}") # o [len(nome)mostra o tamnaho do nome que o usuario digitou
# O -1 pede para ele digitar o ultimo nome, ou seja quando acabar ele pega o ultimo
