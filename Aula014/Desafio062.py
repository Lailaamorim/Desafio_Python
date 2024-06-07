#Melhore o DESAFIO 061. perguntando para o usuário se ele quer mostrar mais alguns termos. 
#O programa encerra quando ale disser que quer mostrar O termos.

print("Gerador de PA")
print("-=" * 15)

primeiro = int(input("Primeiro Termo: "))
razão =  int(input("Razão da PA: "))

termo = primeiro  # Inicializa a variável 'termo' com o valor do primeiro termo da PA
cont = 1  # Inicializa o contador 'cont' com 1
total = 0  # Inicializa a variável 'total' que armazena o número total de termos mostrados
mais = 10  # Inicializa a variável 'mais' com 10, representando o número de termos a serem exibidos inicialmente

# Loop para gerar e exibir termos da PA até que 'mais' seja 0
while mais != 0:  # Continua o loop enquanto 'mais' for diferente de 0
    total = total + mais  # Atualiza o total de termos a serem mostrados
    while cont <= total:  # Loop interno para exibir os termos da PA até alcançar o total desejado
        print(f"{termo} → ", end="")  # Imprime o termo atual da PA, seguido por uma seta, sem quebrar a linha
        termo += razão  # Atualiza o valor de 'termo' adicionando a razão da PA
        cont += 1  # Incrementa o contador
    print("PAUSA")  # Imprime "PAUSA" após exibir os termos atuais
    mais = int(input("Quantos termos você quer mostrar a mais? "))  # Solicita ao usuário quantos termos adicionais ele quer ver
print(f"Progressão finalizada com {total} termos mostrados.")  # Exibe uma mensagem indicando o fim da progressão e o total de termos mostrados