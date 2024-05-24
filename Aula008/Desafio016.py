#Crie um programa que leia um número real qualquer pelo teclado 
#e mostre na tela a sua porção inteira.

#Ex:
# Digite um número:6.127 tem a parte inteira 6.
from math import trunc
num= float(input("Digite um número para saber sua porção inteira : "))
print (f"O valor digitado foi {num} e a sua porção inteira é {trunc(num)}")
