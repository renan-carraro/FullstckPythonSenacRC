# Atividade Prática: Sistema de uma Biblioteca
# '''
# Contexto:
# Você foi contratado para desenvolver um sistema de gerenciamento de biblioteca usando POO em Python.
# O sistema deve modelar livros, usuários e empréstimos, com funcionalidades básicas de cadastro, consulta e operações.

# Requisitos:
# - O sistema deve permitir o cadastro de livros, usuários e empréstimos.
# - O sistema deve permitir a consulta de livros cadastrados.
# - O sistema deve permitir a consulta de usuários cadastrados.
# '''

# DESAFIO (opcional) Classe LivroDigital:
# Herde de Livro e adicione o formato do e-book e formas de download.
class meus_livros:
    '''esqueleto pra lista'''
    def __init__(self,livros,usuario,emprestimo,quantidade):
        self.livros = livros
        self.usuario = usuario
        self.emprestimo =emprestimo
        self.quantidade = quantidade
    def adicionar_livros (self,titulo,autor):
        livros ={"titulo",titulo,"autor"}