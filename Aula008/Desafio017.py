# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, 
#calcule e mostre o comprimento da hipotenusa

#MANEIRA MATEMATICA

#co = float(input("Comprimento do cateto oposto: "))
#ca = float(input("Comprimento do cateto adjacente: "))
##print(f"A hipotenusa vai medir {hi:.2f}")

#MANEIRA COM IMPORTAÇÃO
import math

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))

hi = math.hypot(co, ca)
print(f"A hipotenusa vai medir {hi:.2f}")
