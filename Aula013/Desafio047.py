'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''

# Loop que vai de 1 a 49 (50 não é incluído)
for numero in range(1,51):
    # Verifica se o número é par
    if numero % 2 == 0 :
        # Se o número for par, imprime-o
        print(numero)
print("ACABOU")     

'''For n in range(2,51 ,2):
    print (n, end='')
print("Acabou")    '''   