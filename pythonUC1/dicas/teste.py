import turtle
#tela que vai aparecer teste 60
tela= turtle.Screen()
tela.bgcolor("Black")
tela.title("Um cachorro")
#corpo do cachorro
quadrado= turtle.Turtle()
quadrado.shape("circle") #forma do corpo
quadrado.color("white") #cor do corpo
quadrado.speed(2)
#os movimentos que vai fazer
for i in range(4):
    quadrado.forward(100) # ta andando pra frente
    quadrado.left(90) #ta andado pro lado esquerdo
#o rabinho do dog
quadrado.penup()
quadrado.goto(-50,50)
quadrado.pendown()
quadrado.color("white")
quadrado.forward(100)
#fizalizar o desenho ou loop não entedi isso direito
tela.mainloop()
