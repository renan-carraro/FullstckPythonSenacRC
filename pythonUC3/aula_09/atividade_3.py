class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class GerenciadorUsuarios:
    def __init__(self):
        self.usuarios = {}

    def cadastrar(self, usuario):
        if usuario.email in self.usuarios:
            raise ValueError("Usuário já cadastrado.")
        self.usuarios[usuario.email] = usuario

    def buscar_por_email(self, email):
        return self.usuarios.get(email, None)

    def remover(self, email):
        if email in self.usuarios:
            del self.usuarios[email]
        else:
            raise ValueError("Usuário não encontrado.")

    def atualizar(self, email, nome=None):
        usuario = self.usuarios.get(email)
        if not usuario:
            raise ValueError("Usuário não encontrado.")
        if nome:
            usuario.nome = nome

    def listar_todos(self):
        return list(self.usuarios.values())

