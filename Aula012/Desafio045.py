'''Cria um programa que faça o computador jogar Jokanpô com você.'''

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')

cores = {
    'amarelo':  '\033[0;33m',
    'lilas':'\033[0;35m',
    'verde':'\033[0;32m',
    'vermelho':'\033[0;31m',
    'azul': '\033[0;34m',
    'limpar':'\033[m'             
    }


print('''Suas opções:
[ 0 ] PEDRA 
[ 1 ] PAPEL
[ 2 ] TESOURA
''') 

computador = randint(0, 2) #Entre 0 e 2

while True: 
    resposta = input("PREPARADO PARA COMEÇAR? (Sim/não): ").strip().lower()
    if resposta == "sim":
        jogador = int(input("Qual é a sua jogada: "))
        
        if jogador not in [0, 1, 2]:
            print(f"{cores['azul']}JOGADA INVÁLIDA!{cores['limpar']}")
            continue
        
        
        print('-=' * 20)
        print(f"Computador jogou {(itens[computador])}")
        print(f"Jogador jogou {(itens[jogador])}")
        print('-=' * 20)
        
        if computador == 0: #Computador jogou pedra
            if jogador == 0:
                print(f"{cores['lilas']}EMPATE{cores['limpar']}")
            elif jogador == 1:
                print(f"{cores['verde']}JOGADOR VENCE{cores['limpar']}") 
            elif jogador == 2:
                print(f"{cores['amarelo']}COMPUTADOR VENCE{cores['limpar']}")        
        
        elif computador == 1: #Jogador jogou papel 
            if jogador == 0 :
                print(f"{cores['amarelo']}COMPUTADOR VENCE{cores['limpar']}")
            elif jogador == 1:
                print(f"{cores['lilas']}EMPATE{cores['limpar']}")
            elif jogador == 2  :
                print(f"{cores['verde']}JOGADOR VENCE{cores['limpar']}") 
        
        elif computador == 2: 
            if jogador == 0:
                print (f"{cores['verde']}JOGADOR VENCE{cores['limpar']}")
            elif jogador == 1:
                print(f"{cores['amarelo']}COMPUTADOR VENCE{cores['limpar']}")
            elif jogador == 2:
                print(f"{cores['lilas']}EMPATE{cores['limpar']}") 

    elif resposta == "não":
        print("Saindo do game...")
        break
    else:
        ("Opção inválida digite 'Sim' ou 'Não' ")                                             