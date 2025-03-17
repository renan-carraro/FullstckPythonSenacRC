import turtle

# Configuração da tela
tela = turtle.Screen()
tela.bgcolor("lightblue")
tela.title("Criando um Gato")

# Criando o "gato"
gato = turtle.Turtle()
gato.shape("circle")  # Forma personalizada para o corpo do gato
gato.color("gray")    # Cor do corpo
gato.speed(5)

# Adicionando movimento do "gato"
for _ in range(4):  
    gato.forward(100)  # Anda para frente
    gato.left(90)      # Gira para a esquerda

# Adicionando a cauda
gato.penup()
gato.goto(-50, 50)  # Movendo a tartaruga para outra posição
gato.pendown()
gato.color("black")
gato.forward(50)

# Finaliza o desenho
tela.mainloop()
