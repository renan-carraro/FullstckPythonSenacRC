import turtle

# Configurando o cenário
tela = turtle.Screen()
tela.bgcolor("white")
tela.title("Desenhando com Python")

# Criando a "tartaruga"
desenhista = turtle.Turtle()
desenhista.shape("turtle")
desenhista.speed(3)

# Desenhando um quadrado
for _ in range(4):
    desenhista.forward(100)  # Move para frente
    desenhista.right(90)     # Gira 90 graus para a direita

# Finaliza o desenho
turtle.done()
