numero = int(input("qual o numero da contagem regressiva?:"))
for i in range (numero , -1,-1):
    print("contagem:",i)
#####
numero1 = int(input("Digite um número: "))
for i in range(1, 11):
    print(f"{numero1} x {i} = {numero1 * i}")
######
numero2= int(input("digite um numero: ")) #numero do usuario
print(f"numero pares de 1 até{numero2}: ") #numero digitado do usuario que mostra par até 1
for i in range (1, numero2 + 1):
    if i % 2==0 : #verificar ser o numero é par
        print(i)
########
numero3= int(input("digite um numero fatorial: "))
f=1 #fatorial
c=1#contador
while c <= numero3:
    f*=c
    c+=1
print(f"O fatorial do {numero3} é: {f}")
#####
# Varial pra incar o loop
numero4= int(input("Digite um número maior que 10: "))

while numero4 <= 10:  # pra incar o numero inválido
    print("Número inválido. Por favor, tente novamente.")
    numero4 = int(input("Digite um número maior que 10: ")) #retorno do loop

print(" Você digitou o número: ",numero)