import random  

def jogo_da_forca():  
    palavras = ["banana", "abacaxi", "morango", "uva", "laranja", "melancia", "manga", "pera", "kiwi", "coco"]

    palavra_secreta = random.choice(palavras)  
    letras_corretas = set()  
    tentativas = 6  

    while tentativas > 0:  
        # Exibe a palavra com os caracteres descobertos
        palavra_exibida = "".join(letra if letra in letras_corretas else "_" for letra in palavra_secreta)  
        print("\nPalavra: ", palavra_exibida)  

        # Condição de vitória
        if palavra_exibida == palavra_secreta:  
            print("Parabéns! Você venceu!")  
            return  

        # Permitir que o jogador tente adivinhar a palavra completa
        resposta = input("Se quiser, digite a palavra inteira ou pressione Enter para continuar: ").strip().lower()
        if resposta:
            if resposta == palavra_secreta:
                print("Parabéns! Você acertou a palavra!")
                return
            else:
                print("Que pena! Você errou a palavra e perdeu o jogo.")
                return  # Encerrar o jogo imediatamente se errar

        # Entrada do usuário, garantindo que ele só possa digitar uma única letra válida
        letra = input("Digite uma letra: ").strip().lower()  
        if not letra.isalpha() or len(letra) != 1:  
            print("Por favor, digite apenas uma letra válida.")  
            continue  

        # Verifica se a letra já foi usada
        if letra in letras_corretas:  
            print("Você já tentou essa letra.")
            continue  # Volta para o início do loop sem descontar tentativa  

        # Verifica se a letra está na palavra secreta
        if letra in palavra_secreta:  
            letras_corretas.add(letra)  
            print("Letra correta!")  
        else:  
            tentativas -= 1  
            print(f"Letra incorreta! Tentativas restantes: {tentativas}")  

    print(f"Game over! A palavra era: {palavra_secreta}")  

jogo_da_forca()
