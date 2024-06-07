'''
Cria um programa que simule o Funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será 
o valor a ser sacado (número inteiro) a o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 R41
'''    
total = int(input('Digite um valor inteiro: '))  # Solicita ao usuário que digite um valor inteiro

# Loop for para iterar sobre os valores das cédulas
for i in (50, 20, 10, 1):
    tced = 0  # Inicializa o contador de cédulas para cada valor
    
    # Loop while para decompor o valor em cédulas do valor atual (i)
    while total >= i:
        total -= i  # Subtrai o valor da cédula atual do total
        tced += 1  # Incrementa o contador de cédulas do valor atual
    
    # Se foram retiradas cédulas deste valor, exibe o número total de cédulas
    if tced != 0:
        print(f'Total de cédulas de R$ {i}: {tced}')
