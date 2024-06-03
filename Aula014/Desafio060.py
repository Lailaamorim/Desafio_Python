#Faça um programa que leia um número qualquer a mostre o seu fatorial.

#Ex: 5 = 5x4x3x2x1 = 120

from math import factorial
n = int(input("Digite um numero para calcular seu fatorial: "))
f = factorial(n)
print("O fatorial de {n} é {f}")