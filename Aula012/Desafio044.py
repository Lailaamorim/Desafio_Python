'''Elabora um programa que calcule o valor a ser pago por um produto.
considerando o sau preço normal a condição de pagamento:

- à vista dinheiro/ cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartãO:
praso normal
- 3x ou mais no cartão 20% de juros'''

# Exibe o nome da loja
print("LOJAS LAILA")

# Solicita ao usuário que insira o preço das compras e converte a entrada para um valor float
preco = float(input("Preço das compras: R$ "))

# Exibe as opções de formas de pagamento
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque 
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
    ''')

opcao = int(input("Qual é a opção? "))

# Condicional para calcular o total com base na opção escolhida
if opcao == 1:
    # Desconto de 10% para pagamento à vista em dinheiro ou cheque
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    # Desconto de 5% para pagamento à vista no cartão
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    # Sem desconto, total permanece o mesmo
    total = preco
    # Calcula o valor de cada parcela em caso de pagamento em 2 vezes no cartão, sem juros
    parcela = total / 2
    # Informa ao usuário o valor de cada parcela
    print(f"Sua compra será parcelada em 2x de {parcela} SEM JUROS")
elif opcao == 4:
    # Acrescenta 20% de juros para pagamento em 3 vezes ou mais no cartão
    total = preco + (preco * 20 / 100)
    # Solicita ao usuário o número de parcelas
    totalparcela = int(input("Quantas parcelas? "))
    # Calcula o valor de cada parcela
    parcelas = total / totalparcela
    # Informa ao usuário o valor de cada parcela
    print(f"Sua compra será parcelada em {totalparcela}x de R$ {parcelas:.2f} COM JUROS")
else:
    # Caso a opção inserida seja inválida, o total permanece o mesmo e uma mensagem de erro é exibida
    total = preco
    print("\033[0;31mOPÇÃO INVÁLIDA. Tente novamente!\033[m")

# Exibe o valor total da compra com base na forma de pagamento escolhida
print(f"Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f}")
