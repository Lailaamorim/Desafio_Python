'''• Cria um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, 
mostre a listagem de números gerados e também indique o menor a o maior valor que estão na tupla.'''

from random import randint
numeros = (randint (1, 10),randint (1, 10), randint (1, 10),randint (1, 10), randint (1, 10))
print(f"Os valores sorteados foram: ",end='')
for n in numeros :
    print(f"{n} ",end='')
print(f"\nO maior valor é {max(numeros)}")
print(f"O menor valor é {min(numeros)}")    
