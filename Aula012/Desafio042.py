'''Refaça o DESAFIO 035 dos triângulos. acrescentando o recurso de mostrar que tipo de 
triângulo será formado:

- Equilátero: todos os lados iguais - Isóscales: dois lados iguais

-Escalano: todos os lados diferentes'''

print("-=" * 20)
print("Analisador de triângulos")
print("-=" * 20)

r1 = float(input("Primeiro Segmento: "))
r2 = float(input("Segundo Segmento: "))
r3 = float (input("Teceiro Segmento: "))
# Verificar se os lados formam um triângulo
if r1 < r2  +  r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR UM TRIÂNGULO")
    if r1 == r2 == r3:
        print("EQUILÁTERO!") #todos os lados iguais
    elif r1 != r2 != r3 != r1:  
        print("ESCALENO!") #todos os lados diferentes
    else:     
        print("ISÓSCELES") #dois lados iguais, um diferente
