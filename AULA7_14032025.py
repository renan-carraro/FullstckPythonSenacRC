numero = int(input("digite um numero pra contagem:"))
for i in range (numero , -1,-1): #os numero ele sempre são descatadoou seja,-1 no print vai aparecer 0 (q qualquer numero digitado sera menos um na contagem)
    print("contagem: ",i) 
    ##

numero1 = int(input("Digite um número par:"))
soma = 0
i = 1
while i <= numero1: #while "enquanto"ou meu inicio do loop
    soma += i
    i += 1
print("Soma:", soma)
#####
numero2 = int(input("digite o numero da tabuada: "))
for i in range (numero2,1,11):
    print("contagem:",i)

    numero3 = int(input("Digite um número: "))
for i in range(1, 11):
    print(f"{numero3} x {i} = {numero3 * i}")
######
numero3= int(input("digite um numero fatorial: "))
f=1 #fatorial
c=1#contador
while c <= numero3:
    f*=c
    c+=1
print(f"O fatorial do {numero3} é{f}")
#######
