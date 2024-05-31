'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

import time  # Importa o módulo time, que contém funções para trabalhar com tempo

# Loop para contagem regressiva de 10 até 1
for numero in range (10,-1,-1):
    print(numero)  # Imprime o número atual da contagem regressiva 
    time.sleep(1)  # Pausa a execução do programa por 1 segundo
    
# Imprime a mensagem de celebração após a contagem regressiva terminar    
print("🥳🥳🥳🎉🎉fELIZ FOGOS DE ARTIFÍCIO🥳🥳🥳🎉🎉")