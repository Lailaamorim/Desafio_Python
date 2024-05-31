'''Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando,
um laço for '''

# Solicita ao usuário que digite um número para a tabuada
n = int(input("Digite o número para a tabuada: "))

# Loop que vai de 1 a 9
for numero in range(10):
    # Calcula o valor da tabuada multiplicando o número atual pelo número fornecido
    tabuada = numero * n
    # Imprime o resultado no formato "n X numero = tabuada"
    print(f"{n} X {numero} = {tabuada}")