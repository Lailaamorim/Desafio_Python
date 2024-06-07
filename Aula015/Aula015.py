'''
cont = 1
while cont <= 10: # enquanto for verdade ele vai ficar fazendo até o número estipulado, no caso 10.
    print(cont, '->' , end = '')
    cont += 1
print('Acabou')    

cont = 1
while True: # Desse jeito ele ficará fazendo para sempre até ter uma estrutura de pare 
    print(cont, '->', end='')
    cont += 1
print("Acabou")    
'''
n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n 
print(f"A soma vale {s}")    