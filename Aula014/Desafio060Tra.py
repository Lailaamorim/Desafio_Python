n = int(input("Digite um número para calcular seu Fatorial: "))

c = n # Inicializa a variável 'c' com o valor de 'n'
f = 1 # Inicializa a variável 'f' (fatorial) com 1, pois o fatorial de qualquer número n é multiplicado por cada número de n a 1

print(f"Calculando {n}! = ", end='')
# Loop while para calcular o fatorial
while c > 0: # Continua o loop enquanto 'c' for maior que 0
    print(f"{c}",end='')# Imprime o valor atual de 'c'
    # Adiciona " X " se 'c' for maior que 1, caso contrário, adiciona " = "
    print(" X " if c > 1 else " = ", end='')  
    f *= c # Multiplica 'f' pelo valor atual de 'c' 
    c -= 1 # Decrementa 'c' em 1
print(f"{f}")    
    