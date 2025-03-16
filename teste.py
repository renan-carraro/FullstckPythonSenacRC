palavra=input("digite uma palavra pra verificar ser é um palindromo: ")
palavra= palavra.lower().replace("","")
inverso = palavra[::-1]
if palavra ==inverso:
    print("é um palindromo")
else:
    print("não é um palindromo")