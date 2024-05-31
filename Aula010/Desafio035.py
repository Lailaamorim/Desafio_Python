#Desenvolva um programa que leia o comprimento de três retas 
#e diga ao usuario se elas podem ou não formar um triângulo.

print("-=" * 20)
print("Analisador de Triângulos")
print("-=" * 20)
# Exibe uma linha de separação e o título "Analisador de Triângulos"

r1 = float(input("Primeiro Segmento: "))
r2 = float(input("Segundo Segmento: "))
r3 = float(input("Terceiro Segmento: "))
# Solicita ao usuário que insira os comprimentos dos três segmentos e os converte para valores float

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    # Verifica se a soma de cada par de segmentos é maior que o terceiro segmento
    print("Os segmentos acima PODEM FORMAR UM TRIÂNGULO!")
    # Se todas as condições forem atendidas, imprime uma mensagem informando que os segmentos podem formar um triângulo
else:
    print("Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!")
    # Se alguma das condições não for atendida, imprime uma mensagem informando que os segmentos não podem formar um triângulo
