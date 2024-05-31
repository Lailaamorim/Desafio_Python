'''Escreva um programa que leia um número inteiro qualquer a peça para o usuário escolher 
qual será a base de conversÃO:

- 1 para binário
- 2 para octal
- 3 para hexadecimal'''

num = int(input("Digite um número inteiro: "))

print('''Escolha uma das bases para conversão: 
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
# Exibe as opções de conversão disponíveis

opcao = int(input("Sua opção: "))

if opcao == 1: 
    print(f"{num} Convertido para BINÁRIO é igual a {bin(num)[2:]}")
    # Se a opção escolhida for 1, converte o número para binário e exibe o resultado
elif opcao == 2: 
    print(f"{num} Convertido para OCTAL é igual a {oct(num)[2:]}")
    # Se a opção escolhida for 2, converte o número para octal e exibe o resultado
elif opcao == 3:
    print(f"{num} Convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
    # Se a opção escolhida for 3, converte o número para hexadecimal e exibe o resultado
else:
    print("Opção inválida. Tente novamente.")
    # Se a opção escolhida não estiver entre 1, 2 ou 3, exibe uma mensagem de opção inválida
