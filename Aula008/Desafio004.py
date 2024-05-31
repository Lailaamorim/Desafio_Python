
#Desafio 4

# Solicita ao usuário que digite algo e armazena na variável x
x = (input('DIGITE ALGO :)'))

print('Irei dizer alguns tipos de {}'.format(x))
print('Tipo de', x, 'é', type(x))# Imprime o tipo da variável x utilizando a função type()
print(x .isalnum(), 'é número ou letra.')# Verifica se o conteúdo de x é alfanumérico (letras ou números)
print( 'está maiúsculo?', x .isupper())# Verifica se o conteúdo de x está todo em letras maiúsculas
print('é letra?', x .isalpha())# Verifica se o conteúdo de x é composto apenas por letras
print('é numérico?', x .isnumeric())# Verifica se o conteúdo de x é numérico