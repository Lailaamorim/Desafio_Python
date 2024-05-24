'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
import time
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

#Verificando quem é o menor
menor =  a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
    
# verificando quem é maior  

maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print("Analisando...")
time.sleep(1)
print(f"O menor valor digitado é {menor}")    
print(f"O maior valor digitado é {maior} ") 
               