
sexo = input("Informe seu sexo: [M/F]: ").strip().upper()  #strip() remove espaços em branco nas extremidades, 
#upper() converte para maiúsculas
while sexo not in 'MF':  # while cria um loop que continua enquanto a condição (sexo não está em 'M' ou 'F') for verdadeira
    # Solicita novamente a entrada do usuário caso os dados sejam inválidos
    sexo = input("Dados inválidos. Por favor, informe seu sexo: ").strip().upper()  # Recoleta a entrada do usuário da mesma maneira
# Mensagem de confirmação de registro bem-sucedido
print(f'Sexo {sexo} registrado com sucesso')  # print() exibe a mensagem formatada, f-string inclui o valor da variável sexo na string
