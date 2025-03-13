#Cálculo de Desconto em uma Loja Declare duas variáveis, preco e desconto, com valores 150.0 e 20, respectivamente. Calcule o preço final após aplicar o desconto e imprima o resultado.
preco = float(input("digite seu peso: "))
desconto =float(input("digite seu desconte: "))
preco_final= preco-desconto
print("preço:",preco_final )

###

#Cálculo de IMC (Índice de Massa Corporal) Declare duas variáveis, peso e altura, com valores 70 e 1.75, respectivamente. Calcule o IMC usando a fórmula: IMC = peso / (altura ** 2). Imprima o resultado.

peso = float(input("seu peso: "))
altura =float(input("sua altura: "))
valor = peso / (altura ** 2)
print("o valor",valor)

###

#Verificação de Elegibilidade para um Concurso Declare duas variáveis, idade e tem_experiencia, com valores 22 e True, respectivamente. Verifique se a pessoa é elegível para o concurso (idade maior ou igual a 18 e tem experiência) e imprima o resultado.

tem_experiencia =True
idade=17
idade_maior =idade >=18 and tem_experiencia
print("pode ir", idade_maior)

###

#Classificação de Níveis de Acesso Declare uma variável nivel_acesso com um valor entre 1 e 3. Use estruturas condicionais para imprimir
#"Acesso total" se o nível for 3. "Acesso parcial" se o nível for 2. "Acesso restrito" se o nível for 1


acesso_total = int(input("nivel de acesso: "))
if acesso_total==3:
    print("acesso total")
elif acesso_total==2:
    print("acesso_pacial")
elif acesso_total==1:
    print("acesso restrito")
else:
    print("digite um numero valido")

###
 
#Conversão de Temperatura Declare uma variável celsius com um valor de temperatura em graus Celsius. Converta a temperatura para Fahrenheit usando a fórmula: F = (C * 9/5) + 32. Imprima o resultado.
c =float(input("temperatura em celsius: "))
f= (c * 9/2) +32
print("a temperatura em fahrenheit é: ", f)


##

# Verificação de Números Pares e Ímpares:
#Declare uma variável numero com um valor inteiro. Use estruturas condicionais para verificar se o número é par ou ímpar e imprima o resultado.'''

numero =float(input("digite um numero:"))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


#Cálculo de Frete com Base no Peso Declare uma variável peso com o peso de um pacote em kg. Calcule o frete com base nas seguintes regras:

peso= int(input(qual o peso do pacote: ))

if peso <= 1:
    frete= 10.00
elif 1 < peso <= 5:
    frete = 20.00
elif 5 < peso <= 10:
    frete = 30.00
else:
    frete = 50.00
    print(f"O peso do pacote é {peso} kg. O valor do frete é R$ {frete:.2f}.")