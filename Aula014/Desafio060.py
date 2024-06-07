#Faça um programa que leia um número qualquer a mostre o seu fatorial.

#Ex: 5 = 5x4x3x2x1 = 120

from math import factorial  # Importa a função factorial do módulo math

n = int(input("Digite um número para calcular seu fatorial: ")) 

# Calcula o fatorial do número fornecido pelo usuário
f = factorial(n)  # Utiliza a função factorial para calcular o fatorial de n

# Exibe o resultado
print(f"O fatorial de {n} é {f}") 
