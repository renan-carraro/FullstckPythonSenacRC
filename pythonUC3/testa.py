import random
palavras = { "frutas": ["banana", "abacaxi", "morango", "uva", "laranja", "melancia", "manga", "pera", "kiwi", "coco"]}
palavras1={ "animal": ["elefante", "cachorro", "gato", "tigre", "jacaré", "leão", "pato", "papagaio", "coelho", "rinoceronte"]}
palavras2={"pais": ["brasil", "argentina", "portugal", "japão", "canadá", "frança", "itália", "alemanha", "espanha", "méxico"]}
palavras3={"objeto": ["cadeira", "mesa", "relógio", "telefone", "lápis", "caneta", "carro", "bicicleta", "fogão", "espelho"]}
palavras4={"profissao": ["engenheiro", "médico", "professor", "advogado", "artista", "cozinheiro", "piloto", "jornalista", "bombeiro", "cientista"]}
#print(list(palavras.keys()))

palavras_secreta= random.choice(palavras)
palavras_secreta1=random.choice(palavras1)
palavras_secreta2= random.choice(palavras2)
palavras_secreta3= random.choice(palavras3)
palavras_secreta4= random.choice(palavras4)

