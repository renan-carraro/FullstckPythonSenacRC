import turtle

# Configurando o cenário
tela = turtle.Screen()
tela.bgcolor("white")
tela.title("uma tartaruga")

# Criando a "tartaruga"
desenhista = turtle.Turtle()
desenhista.shape("turtle")
desenhista.speed(3)

# Desenhando um quadrado
for i in range(4):
    desenhista.forward(100)  # Move para frente
    desenhista.right(90)     # Gira 90 graus para a direita

# Finaliza o desenho
turtle.done()
