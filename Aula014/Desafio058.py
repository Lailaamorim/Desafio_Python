# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 a 10. 
# Só que agora o jogador vai tantar adivinhar até acertar, mostrando no final quantos 
# palpitas foram necessários para vencer.

'''Ex:
Foi o numero tal? não
foi o numero tal? não 
foi o numero tal? sim.
parabens '''

from random import randint

computador = randint(0,10)

print("Sou seu computador e acabei de pensar em um número de 0 a 10.")
print ("Será que você consegue adivinhar qual foi?")
acertou = False
palpites = 0
#Loop até o jogador acertar
while not acertou:
    jogador =  int(input("Qual é o seu palpite? "))
    palpites += 1
    #Verifica se o palpite está correto
    if jogador == computador:
        acertou = True
    else :
        if jogador < computador:  
            print("Mais... Tente mais uma vez.")   
        elif jogador  > computador:  
            print("Menos... Tente mais uma vez.")    
print(f"Parabéns! Você acertou o número {computador} em {palpites} palpites" )
