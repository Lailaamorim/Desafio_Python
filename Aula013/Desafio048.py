'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos 
de três e que se encontram no intervalo de de 1 até 500.
'''

# Inicializa a variável para armazenar a soma
soma = 0
# Percorre todos os números de 1 a 500
for numero in range(1, 501, 2):# vai de um até 500 pulando de 2 em 2 
    if numero % 3 == 0:
        cont = cont + 1 
        soma = soma + numero
print(f"A soma de todos os {cont} números ímpares múltiplos de três no intervalo de 1 a 500 é:", soma)
'''
numero % 3 == 0: Verifica se o número é múltiplo de 3. Um número é múltiplo de 3 se o resto da divisão 
por 3 for 0.'''       