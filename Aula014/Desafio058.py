# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 a 10. 
# Só que agora o jogador vai tantar adivinhar até acertar, mostrando no final quantos 
# palpitas foram necessários para vencer.

'''Ex:
Foi o numero tal? não
foi o numero tal? não 
foi o numero tal? sim.
parabens '''

import random

computador = random.randint

palpite = 0
acertou = False

print("O computador escolheu um número entre 0 e 10. Tente adivinhar!")

#Loop até o jogador acertar
while not acertou:
    palpite =  int(input("Qual é o seu palpite? "))
    palpite += 1
    
    #Verifica se o palpite está correto
    if palpite == computador :
        acertou = True
        print(f"Parabéns! Você acertou o número {computador} em {palpite} palpites" )
    else:
        print("Não foi dessa vez. Tente novamente.")    
