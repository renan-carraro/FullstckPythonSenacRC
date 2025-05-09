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
class Livro:
    """Representa um livro na biblioteca."""
    def __init__(self, titulo, autor, categoria):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.disponivel = True  # Corrigido o nome do atributo

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.categoria} {'(Disponível)' if self.disponivel else '(Indisponível)'}"

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = {}  # Transformado em um dicionário para facilitar a gestão de empréstimos

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, nome):
        if nome not in self.usuarios:
            self.usuarios[nome] = []  # Cada usuário tem uma lista de livros emprestados

    def emprestar_livro(self, nome_usuario, titulo_livro):
        if nome_usuario not in self.usuarios:
            return "Usuário não cadastrado."
        
        for livro in self.livros:
            if livro.titulo == titulo_livro and livro.disponivel:
                livro.disponivel = False
                self.usuarios[nome_usuario].append(livro)
                return f'Livro "{titulo_livro}" foi emprestado para {nome_usuario}.'

        return "Livro indisponível ou não encontrado."

    def devolver_livro(self, nome_usuario, titulo_livro):
        if nome_usuario not in self.usuarios:
            return "Usuário não cadastrado."

        for livro in self.usuarios[nome_usuario]:
            if livro.titulo == titulo_livro:
                livro.disponivel = True
                self.usuarios[nome_usuario].remove(livro)
                return f'Livro "{titulo_livro}" foi devolvido por {nome_usuario}.'

        return "Livro não encontrado nos empréstimos do usuário."

    def listar_livros_disponiveis(self):
        return [str(livro) for livro in self.livros if livro.disponivel]

# Exemplo de uso
biblioteca = Biblioteca()
livro1 = Livro("O Senhor dos Anéis", "J.R.R Tolkien", "Fantasia")
livro2 = Livro("lupam", "Leblanc", "Fantasia")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.cadastrar_usuario("rc")

print(biblioteca.emprestar_livro("rc", "lupam"))
print(biblioteca.listar_livros_disponiveis())
print(biblioteca.devolver_livro("rc", "lupam"))
print(biblioteca.listar_livros_disponiveis())
