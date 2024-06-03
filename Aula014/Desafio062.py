#Melhore o DESAFIO 061. perguntando para o usuário se ele quer mostrar mais alguns termos. 
#O programa encerra quando ale disser que quer mostrar O termos.

print("Gerador de PA")
print("-=" * 15)
primeiro = int(input("Primeiro Termo: "))
razão =  int(input("Razão da PA: "))
termo = primeiro 
cont = 1 
total = 0
mais = 10
while mais != 0:
    total = total + mais 
    while cont <= total:
        print(f"{termo}  → ", end="")
        termo += razão
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f"Progressão finalizada com {total} termos mostrados.")    