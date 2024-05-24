'''Escreva um programa que faça o computador "Pensar" em um número inteiro entre 0 e 5 e peça para que o usuário
tentar descobirir qual foi o número escolhido pelo computador '''

#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random# O computador pensa em um número aleatório 
import time


limite= 5 # Definindo o limite superior do intervalo
numero_secreto = random.randint(0, limite) #Usa random.randint para gerar um número aleatório entre 0 e limite_superior.
Tentativas = 0 # Vaiável para controlar o número de tentativas

while True:
# Obtendo o palpite do usuário
    print("-=-" *10)
    palpite = int(input(f"Digite seu palpite (tentativa {Tentativas + 1}): "))
    print("-=-" *10)
    
    #verificando se o palpite está correto 
    print("Analizando...")
    time.sleep(1)  
    if palpite == numero_secreto:
        print(f"Parabéns! Você adivinhou o número em {Tentativas + 1} Tentativas!")
        break
    elif palpite < 0 or palpite > limite:
        print(f"O palpite deve ser entre 0 e {limite}, tente novamente!")
    elif palpite < numero_secreto:
        print(f"O número que você pensou é menor que o número secreto.")
    else:
        print("O número que você pensou é maior que o número secreto.")    
        
    Tentativas += 1           
    
'''
1° Loop while infinito: O loop while agora não possui uma condição de parada específica, 
permitindo que o usuário faça tentativas ilimitadas até acertar o número.

2° Contador de tentativas: A variável tentativas é incrementada a cada iteração do loop,  
armazenando o número total de tentativas do usuário.

3° Mensagem atualizada: A mensagem que informa o número da tentativa foi atualizada para mostrar o valor 
de tentativas + 1, facilitando a contagem para o usuário.



'''