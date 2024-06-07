# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 a 10. 
# Só que agora o jogador vai tantar adivinhar até acertar, mostrando no final quantos 
# palpitas foram necessários para vencer.

'''Ex:
Foi o numero tal? não
foi o numero tal? não 
foi o numero tal? sim.
parabens '''

from random import randint

computador = randint(0, 10)  
# Gera um número aleatório entre 0 e 10 e o atribui à variável 'computador'.

print("Sou seu computador e acabei de pensar em um número de 0 a 10.")
print("Será que você consegue adivinhar qual foi?")

acertou = False  
# Inicializa a variável 'acertou' como False. Esta variável será usada para controlar o loop.
palpites = 0  
# Inicializa a contagem de palpites em 0.

# Loop até o jogador acertar
while not acertou:  
    jogador = int(input("Qual é o seu palpite? "))  
    palpites += 1  
    # Incrementa o contador de palpites a cada tentativa.
    
    # Verifica se o palpite está correto
    if jogador == computador:  
        # Se o palpite for igual ao número gerado pelo computador, o jogador acertou.
        acertou = True  
        # Define 'acertou' como True para sair do loop.
    else:
        if jogador < computador:  
            # Se o palpite for menor que o número gerado pelo computador:
            print("Mais... Tente mais uma vez.")  
            # Informa ao jogador que o número é maior e pede para tentar novamente.
        elif jogador > computador:  
            # Se o palpite for maior que o número gerado pelo computador:
            print("Menos... Tente mais uma vez.")  
            # Informa ao jogador que o número é menor e pede para tentar novamente.

print(f"Parabéns! Você acertou o número {computador} em {palpites} palpites")  
# Quando o loop termina (o jogador acertou), exibe uma mensagem de parabéns com o número correto e a quantidade de palpites.
