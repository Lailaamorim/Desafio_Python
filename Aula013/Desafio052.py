'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

#solicita uma variável para contar o número de divisores
numero = int(input("Digite um número inteiro: "))

#inicializa uma variável para contar o número de divisores 
total_divisores = 0

#Loop para verificar todos os números de 1 até o número inserido 
for i in range(1, numero + 1):
    #verifica se o número atual (i) é um divisor do número inserido 
    if numero % i == 0 :
        # Incremento o contador de divisores 
        total_divisores += 1
#Verifica se o número tem exatamente 2 divisores (1 e ele mesmo )
if total_divisores == 2:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")            
            
