lanche = ("Hamburgue", "Suco","Pizza","Pudim") 
        #      0         1      2         3
        #Tuplas são imutavéis => Os objetos do tipo tupla não podem ter itens assimilados (Não pode atribuir mais coisas nela
        # durante o programa, só se refazer novamente do inicio )
print(lanche) # Mostra a lista toda
print(lanche[2]) # Mostra o elemento "Pizza"
print(lanche[0:2]) # Mostra da posição 0 até a 2 => "Hamburgue","Suco" porem não mostta a pizza pq o fatiamneto
#Sempre ignora a ultima posição
print(lanche[1:]) #Mostra "Suco", "Pizza", Pudim Significa para ir do elemento 1 até o final
print(lanche[:2]) #mostra do inicio até o dois
print(lanche[-1]) # Mostra "Pudim", o Ultimo elemento do lanche como -2 seria a pizza, -3 o suco, -4 é o hamburgue
print(len(lanche)) # Ele dirá quantos elementos tem o lanche "4"
print("-="*15)
for comida in lanche: #o for que usei como range, agora estou usando como itens
    print(f"Eu vou comer {comida}")
print("Comi pra caramba!")  

for cont in range(0, len(lanche)):
    print(f"Eu vou comer muito {lanche} na posição {cont}")  
    
for posição, comida in enumerate (lanche):
    print(f"Eu vou comer {comida} na posição posição {posição}  ")    
    
print(sorted(lanche)) # O sorted coloca a tupla em ordem