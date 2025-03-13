while True: #inicio do loop
    try:
        acesso_total = int(input("nivel de acesso: "))
        if acesso_total==3:
            print("acesso total")
        elif acesso_total==2:
            print("acesso_pacial")
        elif acesso_total==1:
            print("acesso restrito")
        else:  
            print("digite um numero valido")
            continue #vai ficar em loop ate achar um resutado correto
        break #final do loop
    except ValueError: #erro ser tiver pedindo
        print("erro digite somente numeros")