while True:
    try:
        c=float(input("temperatura em celsius: "))
        f= (c * 9/2) +32
        break
    except ValueError:print("digite apenas numeros!")
print("a temperatura em fahrenheit é: ", f)