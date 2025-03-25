a = 10
b = 5
print("soma:", a + b)
print("subtração:", a - b)
print("multiplicação:", a * b)
print("divisão", a / b) 

primeiro_nome = "maria"
sobrenome = "silva"
nome_completo = primeiro_nome + " " + sobrenome
print(nome_completo)

x =15
y =20
print("x é maior que y?", x > y)
print("x é igual a y?", x == y)

tem_carteira = True
idade =18
tem_carro = False
pode_dirigir = idade >= 18 and tem_carteira 
print("pode dirigir", pode_dirigir)
print("pode dirigir e tem carro?",pode_dirigir and tem_carro)

#AND pra dizer que precisa ser 2 dois verdadeiro pra constar verdade,OR precisa ter uma verdader pra contar,NOT torna verdade em falso
frase = "Python é divertido"
print(frase.upper()) #upper() pra diz em maiuscolo lower em minuscula
nova_frase = frase.replace("divertido","poderoso",) #replace é pra subistituir
print(nova_frase)

contador = 0
contador += 5 #contador =contador+5 (+=)são a mesma coisa
contador -= 2 #contador =contador-2
contador *= 3 #contador =contador*=3
print("Valor final do contador:", contador)

a = 10 
b = 20
c = 30 
media = (a + b + c) / 3
print("mwdia:",media)
print("A media é maior que 15 e menor que 25?:",15 <media <25)

nota =75
if nota >=60:  #efeito cascata vai lendo a ordem ex, ser minha nota for 75 é a base pra ser aprovado é 60 ele não vai ler o resto ja que acho o resutado,ser for menor ex:41 vai dar recuperação
    print("aprovado")
elif nota >=40:
    print("recuperação")
else:
    print("reprovado")
