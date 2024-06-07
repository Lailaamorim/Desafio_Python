'''
• Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador 
PERDER. mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint  # Importa a função randint do módulo random

v = 0  # Inicializa a variável v para contar o número de vitórias do jogador

while True:  # Loop infinito para permitir que o jogo continue indefinidamente
    jogador = int(input("Diga um valor: ")) 
    
    computador = randint(0, 10)  # Gera um número aleatório para o computador entre 0 e 10
    
    total = jogador + computador  # Calcula o total somando o valor do jogador e do computador
    
    tipo = ' '  # Inicializa a variável tipo para armazenar a escolha do jogador (par ou ímpar)
    
    # Loop enquanto o tipo não for 'P' ou 'I'
    while tipo not in 'PpIi':
        tipo = input("Par ou Impar? [P/I] ").strip().upper()[0]  # Solicita ao jogador que escolha par ou ímpar
    
    # Exibe o resultado da rodada (total e se foi par ou ímpar)
    print(f"Você jogou {jogador} e o computador {computador}. Total deu {total}", end='')
    print(" DEU PAR" if total % 2 == 0 else " DEU ÍMPAR")
    
    # Verifica se o jogador venceu
    if tipo == 'P':  # Se o jogador escolheu par
        if total % 2 == 0:  # E o total é par
            print("Você VENCEU!")  # O jogador venceu
            v += 1  # Incrementa o número de vitórias do jogador
        else:
            print("Você PERDEU!")  # Caso contrário, o jogador perdeu
            break  # O jogo é encerrado
    elif tipo == 'I':  # Se o jogador escolheu ímpar
        if total % 2 == 1:  # E o total é ímpar
            print("Você VENCEU!")  # O jogador venceu
            v += 1  # Incrementa o número de vitórias do jogador
        else:
            print("Você PERDEU!")  # Caso contrário, o jogador perdeu
            break  # O jogo é encerrado
    
    print("Vamos jogar novamente...")  # Exibe uma mensagem para indicar que outra rodada está prestes a começar

print(f"GAMER OVER! Você venceu {v} rodada(s).")  # Exibe uma mensagem final indicando o fim do jogo e o número de vitórias do jogador
