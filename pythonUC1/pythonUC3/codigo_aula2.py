import random

def jogo_da_forca():
    Frutas = ["banana", "abacaxi", "morango", "uva", "laranja", "melancia", "manga", "pera", "kiwi", "coco"]
    Animais = ["elefante", "cachorro", "gato", "tigre", "jacaré", "leão", "pato", "papagaio", "coelho", "rinoceronte"]
    Países = ["brasil", "argentina", "portugal", "japão", "canadá", "frança", "itália", "alemanha", "espanha", "méxico"]
    Objetos = ["cadeira", "mesa", "relógio", "telefone", "lápis", "caneta", "carro", "bicicleta", "fogão", "espelho"]
    Profissões = ["engenheiro", "médico", "professor", "advogado", "artista", "cozinheiro", "piloto", "jornalista", "bombeiro", "cientista"]

    listas = [Frutas, Animais, Países, Objetos, Profissões]
    categorias = ["Frutas", "Animais", "Países", "Objetos", "Profissões"]

    lista_escolhida = random.choice(listas)
    palavra_secreta = random.choice(lista_escolhida)
    letras_corretas = set()
    tentativas = 6

    # Exibe dica da categoria
    indice_lista = listas.index(lista_escolhida)
    print(f"A dica é: {categorias[indice_lista]}")

    while tentativas > 0:
        # Exibe a palavra com os caracteres descobertos.
        palavra_exibida = " ".join(letra if letra in letras_corretas else "_" for letra in palavra_secreta)
        print(f"Palavra: {palavra_exibida}")

        # Caso de vitória
        if set(palavra_secreta) == letras_corretas:
            print("Parabéns! Você venceu!")
            break

        # Tentativa completa da palavra
        resposta = input("Digite a palavra inteira ou pressione Enter para tentar adivinhar uma letra: ").strip().lower()
        if resposta:
            if resposta == palavra_secreta:
                print("Parabéns! Você acertou a palavra!")
                break
            else:
                print("Que pena! Você errou a palavra!")
                break

        # Entrada de usuário para letras, garantindo que ele só possa digitar uma única letra válida
        while True:
            letra = input("Digite uma letra: ").strip().lower()
            if not letra.isalpha() or len(letra) != 1:
                print("Por favor, digite apenas uma letra válida.")
            else:
                break

        # Verifica se a letra está correta
        if letra in palavra_secreta:
            letras_corretas.add(letra)
            print("Letra correta!")
        else:
            tentativas -= 1
            print(f"Letra incorreta! Tentativas restantes: {tentativas}")

    print(f"GAME OVER! A palavra era: {palavra_secreta}")

# Chamando a função para iniciar o jogo apenas uma vez
jogo_da_forca()
