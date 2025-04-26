def verificar_experiencia():
    """Valida a experiência do usuário com entrada 's' ou 'n'."""
    while True:
        resposta = input("Você tem experiência? Digite 's' para sim ou 'n' para não: ").strip().lower()
        if resposta in ('s', 'n'):
            return resposta == 's'  # Retorna True se 's', False se 'n'
        print("Entrada inválida. Por favor, digite apenas 's' ou 'n'.")

def obter_idade():
    """Obtém e valida a idade do usuário como número inteiro."""
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            return idade
        except ValueError:
            print("Erro. Por favor, digite um número válido para a idade.")

def esta_habilitado(idade, experiencia):
    """Verifica se o usuário está habilitado para trabalhar."""
    return idade >= 18  and  experiencia

def main():
    print("Bem-vindo ao programa de verificação de habilitação para trabalho!")
    experiencia = verificar_experiencia()
    idade = obter_idade()
    if esta_habilitado(idade, experiencia):
        print("Você está habilitado(a) a trabalhar.")
    else:
        print("Você não está habilitado(a) a trabalhar.")

# Executa o programa
if __name__ == "__main__":
    main()

        
