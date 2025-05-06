# Criando e escrevendo em um arquivo
with open('usuarios.txt', 'w') as dados:
    dados.write("Nome: renan\nEmail: ranan@email\n")
    dados.write("nome:crossns\nEmail:crossns@gmail\n")
with open('usuarios.txt' ,'r') as dados:
    conteudo=dados.read()
print(conteudo)
with open('dados.txt','a')as arquivo:
    arquivo.write("\nEmail:crossns@gmail\n")
import os
if os.path.exists('dados.txt'):
    os.remove("dados.txt")
    print("arquivo foi de vasco")
else:
    print("arquivo não foi contradado pelo vasco")

 


