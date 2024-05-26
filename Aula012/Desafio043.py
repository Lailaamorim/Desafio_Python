'''Desenvolva uma lógica que leia o peso a a altura de uma pessoa, calcule sau IMC e 
mostre seu status, de acordo com a tabala abaixo:

- Abaixo da 18.5: Abaixo do Peso
- Entre 18.5 a 25: Peso ideal
- 25 até 30: Sobrepeso 
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida'''

peso = float(input("Insira seu peso: (Kg) "))
altura = float(input("Insira sua altura? (m)"))
imc = peso / (altura ** 2)
print(f"O IMC dessa pessoa é de {imc:.1f}")
if imc < 18.5:
    print("Você está ABAIXO DO PESO normal")
elif 18.5 <= imc < 25 :
    print("PARABÉNS, Voc~e está na faixa de PESO NORMAL")  
elif 25 <= imc < 30:
    print('Você está em sobrepeso') 
elif 30 <= imc < 40:
    print("Você está em OBSIDADE, CUIDADO!")      
elif imc >= 40:
    print("Voc~e está em OBSIDADE MÓRBIDA, CUIDADO!")    