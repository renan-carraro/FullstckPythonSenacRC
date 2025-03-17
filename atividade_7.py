while True:
    try:

        peso = int( input("qual o peso do pacote: "))  
        if peso <= 1:
            frete= 10.00
        elif 1 < peso <= 5:
            frete = 20.00
        elif 5 < peso <= 10:
            frete = 30.00
        else:
            frete = 50.00
        break
    except ValueError:print("erro,digite apenas numeros!")
print(f"O peso do pacote é {peso} kg. O valor do frete é R$ {frete:.2f}.")