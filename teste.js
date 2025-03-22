// Criando duas matrizes 3x3
const matrizA = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ];
  
  const matrizB = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
  ];
  
  // Exibindo as matrizes no console
  console.log("Matriz A:", matrizA);
  console.log("Matriz B:", matrizB);
  
  // Soma das matrizes
  const soma = matrizA.map((linha, i) =>
    linha.map((valor, j) => valor + matrizB[i][j])
  );
  console.log("Soma das matrizes:", soma);
  
  // Multiplicação das matrizes
  const multiplicacao = Array(3).fill(0).map(() => Array(3).fill(0)); // Matriz 3x3 zerada
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      for (let k = 0; k < 3; k++) {
        multiplicacao[i][j] += matrizA[i][k] * matrizB[k][j];
      }
    }
  }
  console.log("Multiplicação das matrizes:", multiplicacao);

  ///// minha base//////


  Passo 1: Criando as matrizes
As matrizes são representadas como arrays de arrays em JavaScript. Por exemplo:

javascript
const matrizA = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];
Aqui, matrizA é uma matriz 
3
×
3
, onde:

A primeira linha contém os números 1, 2, 3.

A segunda linha contém os números 4, 5, 6.

E assim por diante.

Passo 2: Exibindo as matrizes
Usamos o console.log para exibir as matrizes no console do navegador ou no terminal:

javascript
console.log("Matriz A:", matrizA);
console.log("Matriz B:", matrizB);
Passo 3: Soma das matrizes
Para somar duas matrizes, percorremos cada elemento de uma matriz e somamos com o correspondente da outra matriz. Isso é feito com o método map:

javascript
const soma = matrizA.map((linha, i) =>
  linha.map((valor, j) => valor + matrizB[i][j])
);
O que acontece aqui:

map percorre cada linha da matriz.

i representa o índice da linha, e j representa o índice da coluna.

A soma é feita elemento por elemento, como 
𝐴
[
0
]
[
0
]
+
𝐵
[
0
]
[
0
]
, 
𝐴
[
0
]
[
1
]
+
𝐵
[
0
]
[
1
]
 e assim por diante.

Resultado: Uma nova matriz que contém a soma elemento por elemento.

Passo 4: Multiplicação das matrizes
Aqui as coisas ficam mais complexas! Para multiplicar duas matrizes, aplicamos a regra:

𝐶
[
𝑖
]
[
𝑗
]
=
∑
𝑘
=
0
𝑛
𝐴
[
𝑖
]
[
𝑘
]
×
𝐵
[
𝑘
]
[
𝑗
]
Isso significa que o elemento na posição 
𝑖
,
𝑗
 da matriz resultante é a soma dos produtos dos elementos correspondentes da linha de 
𝐴
 e da coluna de 
𝐵
.

No código:

javascript
const multiplicacao = Array(3).fill(0).map(() => Array(3).fill(0));
for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    for (let k = 0; k < 3; k++) {
      multiplicacao[i][j] += matrizA[i][k] * matrizB[k][j];
    }
  }
}
O que está acontecendo:

Criamos uma matriz 3x3 inicializada com zeros.

Usamos três loops:

O primeiro (i) percorre as linhas da matriz resultante.

O segundo (j) percorre as colunas da matriz resultante.

O terceiro (k) percorre os elementos da linha de 
𝐴
 e da coluna de 
𝐵
 para realizar a soma dos produtos.

O resultado final é a matriz produto.