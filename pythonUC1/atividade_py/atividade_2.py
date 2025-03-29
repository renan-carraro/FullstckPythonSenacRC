while True: # incio do meu loop
    try:
        peso = float(input("seu peso: "))
        altura =float(input("sua altura: "))
        imc= peso / (altura ** 2) #fromula do imc
        imc_aprocimado= round(imc,2) #somente vai aparecer duas casa decimais
        print("o valor do imc é: ",imc_aprocimado)
        break #final do meu loop
    except ValueError:
        print("Erro!,Por Favor digite apenas numeros e '.'")