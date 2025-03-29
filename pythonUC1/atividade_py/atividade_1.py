while True: # inicio do loop
    try:
        preco = float(input("digite seu preço: "))
        desconto =float(input("digite seu desconto: "))
        preco_final = preco-desconto
        print("preço com desconto: ",preco_final )
        break #saida do loop
    except ValueError: #mostrar o erro em caso seja necessário
        print("Erro,por favor digite um numero. Tentar Novamente?")