#Refaça o DESAFIO 051. lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da 
#progressão usando a estrutura while.

print("Gerador de PA")
print("-=" * 10)

# Solicita ao usuário que insira o primeiro termo e a razão da progressão aritmética (PA)
primeiro = int(input("Primeiro Termo: "))
razão = int(input("Razão da PA: "))
termo = primeiro 
cont = 1

# Loop para gerar e exibir os 10 primeiros termos da PA
while cont <= 10:
    print(f"{termo}", end='') # Adicionado um espaço após cada termo para melhor legibilidade
    termo += razão
    cont += 1
print("Fim")    