import math

num = int(input("Digite um número: "))
raiz = math.sqrt(num)
raiz_arredondada = math.ceil(raiz)

print(f"A raiz quadrada de {num} é aproximadamente {raiz_arredondada}")