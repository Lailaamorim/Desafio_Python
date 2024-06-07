'''
Cria um programa que simule o Funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será 
o valor a ser sacado (número inteiro) a o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 R41
'''    
total = int(input('digite um valor inteiro: '))
for i in (50, 20, 10, 1):
    tced = 0
    while total >= i:
        total -= i
        tced += 1
    if tced != 0:
        print(f'Total de cédulas de R$ {i}: {tced}')