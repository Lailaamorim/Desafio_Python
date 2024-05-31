'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e menor peso.'''

# Inicializando listas para armazenar nomes e pesos
nomes = []
pesos = []

#Loop para coletar dados de cinco pessoas 
for i in range(5):
    nome = input(f"Digite o nome da {i+1}° pessoa:")
    peso = float(input(f"Insira o peso de {nome}: "))
    
    #Armazena dados nas listas
    nomes.append(nome)
    pesos.append(peso)
    '''
    .append(): Este é um método da linguagem Python que é usado para adicionar elementos a uma lista. 
    Ele funciona como se você estivesse colocando o elemento no final da fila.'''
    
#Encontrando o maior é menor peso 
maior_peso = max(pesos)
menor_peso = min(pesos)    

'''As funções max() e min() são utilizadas para encontrar o maior e menor peso entre os valores da lista pesos.
'''
#Encontrando o indice da pessoa com maior peso
indice_maior_peso = peso.index(maior_peso)

#Imprima os resultados 
print(f"\n maior peso foi de {maior_peso: .2f} kg, pertencente a {nomes[indice_maior_peso]}.")
print(f"O menor peso foi de {menor_peso:.2f} kg.")