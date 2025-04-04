while True:  # Início do loop
    try:
        # Pra ser tem experiência
        tem_experiencia = input("Você tem experiência? Digite 's' para sim ou 'n' para não: ").strip().lower()

        if tem_experiencia == "s":
            experiencia = True
        elif tem_experiencia == "n":
            experiencia = False
        else:
            print("Entrada inválida. Digite apenas 's' ou 'n'.")
            continue  # Volta ao início do loop caso a entrada seja inválida

        # idade do usuario
        idade = int(input("Digite sua idade: "))
        break  # Finaliza o loop se tudo estiver correto
    except ValueError:
        print("Erro. Por favor, digite um número válido para a idade.")

# ver ser ta habilitação ao trabalho
idade_maior = idade >= 18 and experiencia

if idade_maior:
    print("Você está habilitado(a) a trabalhar.")
else:
    print("Você não está habilitado(a) a trabalhar.")