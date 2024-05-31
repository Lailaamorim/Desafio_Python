'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda 
não atingiram a maioridade e quantas já são maiores.'''

from datetime import date

#inicializando variáveis 

maiores_idade = []
menores_idade = []

#Loop para ler dados de 7 pessoas 
for i in range(7):
    nome = input (f"Digite o nome da {i + 1}° pessoa: ")
    ano_nascimento = int(input(f"Digite o ano de nascimento de {nome}: "))
    
    #Calcular a idade 
    idade = date.today().year - ano_nascimento
    
    #Verificando se é maior ou menor de idade 
    if idade >= 18: 
        maiores_idade.append(nome)
    else:
        menores_idade.append(nome)
        
#Imprimir Resultados    
print(f"\n**Maiores de idade:**")
for nome in maiores_idade:
    print(f"-{nome}")
        
print(f"\n**Menores de idade:** ")
for nome in menores_idade:
    print(f"- {nome}")
                