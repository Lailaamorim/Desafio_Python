#Crie um programa que leia dois valores a mostre um menu na tela:
'''
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

#inicia com dois valores  

valor1 = int(input("Primeiro número: "))
valor2 = int(input("Segundo número: "))

while True:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior'
    [4] Novos números 
    [5] Sair do programa.
''')
    
    opção = int(input("Escolha uma opção: "))
    
    if opção == 1:
        s = valor1 + valor2 
        print(f"Soma: {valor1} + {valor2} = {s}" )
        
    elif opção == 2:
        m = valor1 * valor2
        print(f"Multiplicação: {valor1} * {valor2}  = {m} ")
        
    elif opção == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            valor2 > valor1
            maior = valor2
        print(f"Valor Maior é: {maior}")    
            
    elif opção == 4  :
        valor1 = int(input("Primeiro número: "))
        valor2 = int(input("Segundo número: ")) 
        
    elif opção == 5:
        print("Saindo do Programa!!")    
        break
    else:
        print("Opção invalida")    