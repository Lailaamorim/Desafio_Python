'''Elabora um programa que calcule o valor a ser pago por um produto.
considerando o sau preço normal a condição de pagamento:

- à vista dinheiro/ cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartãO:
praso normal
- 3x ou mais no cartão 20% de juros'''

print("LOJAS LAILA")
preco = float(input("Preço das compras: R$ "))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque 
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
    ''')

opcao = int(input("Qual é a opção? "))
if opcao == 1:
    total = preco - (preco* 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 /100) 
elif opcao == 3:
    total = preco
    parcela =  total / 2 
    print(f"Sua compra será parecelada em 2x de {parcela} SEM JUROS ")
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparcela = int(input("Quantas parcelas? "))
    parcelas = total / totalparcela
    print(f"Sua compra será parcelada em {totalparcela}x de R$ {parcelas:.2f} COM JUORS")
else :
    total = preco
    print("\033[0;31mOPÇÃO INVÁLIDA. Tente novamente!\033[m")
print(f"Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f}")            
