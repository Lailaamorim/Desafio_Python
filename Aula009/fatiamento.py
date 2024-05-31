#Fatiamento

frase = "A única maneira de aprender é fazendo."
# A   U N I C A   M A  N  E  I  R   A    D  E      A  P  R  E  N  D  E  R      É    F  A  Z   E  N D O.
# 0 1 2 3 4 5 6 7 8 9 10  11 12 13 14 15 16 17 18  19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
print(len(frase)) #Mostra o tamanho da frase (38 caracteres).
print(frase[3])#pega a letra que está na posição 3
print(frase[3:13]) #vai da letra que está no três, até a que esta no número 13
print(frase.count("a"))#conta quantas vezes aparece a letra que está entre parenteses
print(frase.count("a",0,13))# quantas letras "a" tem de zero a treze
print(frase.find("nei"))# Ele vai dizer em que momento na frase começou a palavra mei, nesse caso no posição 10
print(frase.find("Ventura"))# Quando não tem a palavra indicada, ele retorna o valor -1 que significa que a string ão existe
print("unica" in frase)# verá se tem a palavra curso na frase e se sim dirá que é verdade]
print(frase.replace("fazendo ", "praticando"))#Substituie a palavra antiga pela palavra nova
print(frase.upper())# transforma as letras minusculas em maiusculas
print(frase.lower())# transforma as letras mauisculas em minusculas
print(frase.capitalize())# ele tranforma todas as letras maiscusculas em menusculas menos as iniciais 
print(frase.title())# Vai analizar quantas palavras tem na frase e mudar para maicusla a inicial de cada uma delas.
print(frase.strip())#Ele irá remover todos os espaços inúteis no início e no final da string
print(frase.rstrip())#Remove o espaço só no lado direito
print(frase.lstrip())#Remove espaço só no lado esquerdo
print(frase.split()) #  Ele divide a string na variável frase em uma lista de substrings com base em um separador específico. Por padrão, o separador é qualquer espaço em branco, como tabulação ou nova linha.                                                                  
print("_".join(frase))#Coloca um espaço ou um traço em cada palavra 

#.append(): #Este é um método da linguagem Python que é usado para adicionar 
    #elementos a uma lista. Ele funciona como se você estivesse colocando o elemento no final da fila.