while True:
    try:
        numero = float(input("Digite um número: "))
        if numero.is_integer():  # Verifica se o número é inteiro
            if numero % 2 == 0:
                print("O número é par.")
            else:
                print("O número é ímpar.")
        break
    except ValueError: #me retona um erro
        print("Erro! Digite um número válido.")