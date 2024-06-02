'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

numero = int(input("Digite um número inteiro: "))
total_divisores = 0 #inicializa uma variável para contar o número de divisores 
for i in range(1, numero + 1): #Loop para verificar todos os números de 1 até o número inserido
    if numero % i == 0 :   #verifica se o número atual (i) é um divisor do número inserido 
        print('\033[33m', end= ' ')
        total_divisores += 1  # Incremento o contador de divisores 
    else:
        print("\033[31m", end=' ')   
    print(i, end=' ')    
print(f"\n\033[mO Número {numero} foi divisível {total_divisores} vezes. ")     
if total_divisores == 2:       #Verifica se o número tem exatamente 2 divisores (1 e ele mesmo )
    print("O número é PRIMO.")
else:
    print("O número não é PRIMO.")            
            
