'''
Faça um programa que mostra a tabuada de vários números, um de cada vez. para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''
while True:  # Loop infinito
    t = int(input("Quer ver a tabuada de qual valor: "))  # Solicita ao usuário que insira um número para a tabuada
    
    if t < 0:  # Verifica se o número inserido pelo usuário é negativo
        break  # Se for negativo, o loop é interrompido
    
    for n in range(0, 11):  # Loop for para gerar a tabuada do número inserido, indo de 0 a 10
        print(f"{n} X {t} = {t * n}")  # Exibe o resultado da multiplicação
        
print("TABUADA ENCERRADA.")  # Exibe uma mensagem indicando que a tabuada foi encerrada
