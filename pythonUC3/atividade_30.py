#1.Filtre produtos com preço > 1000 usando list comprehension;

produtos = [
    {"nome": "Notebook", "preço": 3500},
    {"nome": "Smartphone", "preço": 2500},
    {"nome": "Fone de ouvido", "preço": 200},
    {"nome": "Monitor", "preço": 1200},
    {"nome": "Teclado", "preço": 300}
]

# Filtrando produtos com preço > 1000
produtos_filtrados = [produto for produto in produtos if produto["preço"] > 1000]

print(produtos_filtrados)

#2.Conte quantos produtos existem por categoria (usar dicionário);

produtos = [
    {"nome": "Notebook", "categoria": "Eletrônicos", "preço": 3500},
    {"nome": "Smartphone", "categoria": "Eletrônicos", "preço": 2500},
    {"nome": "Fone de ouvido", "categoria": "Acessórios", "preço": 200},
    {"nome": "Monitor", "categoria": "Eletrônicos", "preço": 1200},
    {"nome": "Teclado", "categoria": "Acessórios", "preço": 300},
    {"nome": "Cadeira Gamer", "categoria": "Móveis", "preço": 900}
]

# Criando um dicionário para contar os produtos por categoria
contador_categorias = {}

for produto in produtos:
    categoria = produto["categoria"]
    contador_categorias[categoria] = contador_categorias.get(categoria, 0) + 1

print(contador_categorias)

#3.Remova duplicatas de uma lista de pedidos usando set.

comidas = ["Pizza", "Hambúrguer", "Pizza", "Sushi", "Hambúrguer", "Tacos"]

comidas_unicas = list(set(comidas))

print(comidas_unicas)

#4.Uma empresa contratou seus serviços para armazenar dados de colaboradores em memória e realizar operações como:

# Criando uma lista para armazenar os colaboradores
colaboradores = []

# Função para adicionar um colaborador
def adicionar_colaborador(id, nome, salario):
    colaborador = {"id": id, "nome": nome, "salario": salario}  # Criando um dicionário
    colaboradores.append(colaborador)  # Adicionando à lista

# Função para buscar um colaborador pelo ID
def buscar_colaborador_por_id(id):
    for colaborador in colaboradores:
        if colaborador["id"] == id:
            return colaborador
    return None  # Retorna "None" se não encontrar

# Função para listar colaboradores com salário acima de X
def listar_colaboradores_com_salario_acima_de(valor):
    return [colab for colab in colaboradores if colab["salario"] > valor]

# Testando as funções
adicionar_colaborador(1, "Ana", 3000)
adicionar_colaborador(2, "Pedro", 5000)
adicionar_colaborador(3, "Carla", 4000)

print(buscar_colaborador_por_id(2))  # Deve mostrar Pedro
print(listar_colaboradores_com_salario_acima_de(3500))  # Deve mostrar Pedro e Carla