notas=float(input("qual sua nota: ")) #
if notas >=7:
    print("aprovado")
elif notas>=4:
    print("recuperação")
else:
    print("repovado")
#######
numero_inicio=int(input("digite um numero pra iniciar: "))
numero_final= int(input("digite um numero pre finalizar: "))
numero_pares=0
for i in range (numero_inicio , numero_final + 1): #for i in range para meu inicio do loop/(numero_inicio , numero_final + 1): pra incluir no final da contagem do loop
    if i % 2==0: #só pra ver ser ele é par
        numero_pares += i #add o numero na soma
    print(f"soma dos numeros pares no intervalos de {numero_inicio} a {numero_final} é: {numero_pares}")
#############
palavra=input("digite uma palavra pra verificar ser é um palindromo: ")
palavra= palavra.lower().replace("","")# deixa tudo em minusculo só pra ficar bonito no final
inverso = palavra[::-1]
if palavra ==inverso:#pra ver ser a palavra ditada é igual ao inverso ex:arara
    print("é um palindromo")
else:
    print("não é um palindromo")
