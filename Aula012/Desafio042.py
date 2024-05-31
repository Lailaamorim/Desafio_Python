'''Refaça o DESAFIO 035 dos triângulos. acrescentando o recurso de mostrar que tipo de 
triângulo será formado:

- Equilátero: todos os lados iguais - Isóscales: dois lados iguais

-Escalano: todos os lados diferentes'''

print("-=" * 20)
print("Analisador de triângulos")
print("-=" * 20)

r1 = float(input("Primeiro Segmento: "))
r2 = float(input("Segundo Segmento: "))
r3 = float(input("Terceiro Segmento: "))

# Verifica se os segmentos fornecidos podem formar um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR UM TRIÂNGULO")
    # Se os segmentos puderem formar um triângulo, exibe uma mensagem indicando isso
    
    # Classifica o tipo de triângulo
    if r1 == r2 == r3:
        print("EQUILÁTERO!") # Todos os lados iguais
    elif r1 != r2 != r3 != r1:  
        print("ESCALENO!") # Todos os lados diferentes
    else:     
        print("ISÓSCELES") # Dois lados iguais, um diferente
else:
    print("Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO")
    # Se os segmentos não puderem formar um triângulo, exibe uma mensagem indicando isso

