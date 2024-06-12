'''
Cria um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 a 20) a mostrá-lo por extenso.'''
cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 
'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 
'Dezoito','Dezenove', 'Vinte')   

while True:
    n = int(input("Digite um número: entre 0 e 20: "))
    if 0 <= n <= 20 :
        print(f"Você digitou o número {cont[n]}")
    else:    
        print("NÚMERO INVÁLIDO!")
    continuar = input("Deseja Continuar: [S/N]").lower()
    if continuar != 's':
        break




