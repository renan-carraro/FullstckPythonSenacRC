//////1
const matriz1 = [
    [1, 2, 3],//base da matriz
    [4, 5, 6],
    [7, 8, 9]
];
const matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
];
console.log(`primeira matriz: ${matriz1}`); // vai puxar a primeira matriz
console.log(`segunda matriz:${matriz2}`);

const soma = matriz1.map((linha,i)=>
    linha.map((valor,j) => valor +matriz2[i][j])
);
console.log(`A soma das matrizes: ${soma}`);
// multiplicação da matriz
const multiplicacao = Array (3).fill (0).map(() => Array(3).fill(0));// vai deixa a matriz 3x3 limpa
for (let j = 0; j < 3; j++) {//vai ler linha horizontal
    for (let j = 0; j < 3; k++) {// vai ler linha verticall
        for (let k = 0; k < 3; k++){
            multipçicacao[i][j] += matriz1 [i][k] * matriz2[k][j];
        }
    }
}
console.log(`vmultiplicação das matrizes: ${multiplicacao}`);

/////////2

function levarMatriz(matriz){
    return matriz[0].map((_,i) => matriz.map(row => row[i]));
}

const matriz_de_inicio =[//teste resutado:[ [ 1, 4, 7 ], [ 2, 5, 8 ], [ 3, 6, 9 ] ]
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

const matriz_transposta = levarMatriz(matriz_de_inicio);
console.log(matriz_transposta);
console.table(matriz_transposta); // formato pra sair compilada

/////////3

function vezesMatrizes(matriz3,matriz4){
    const resultado =[//começando com zero que vai ser atribuido o valor
        [0, 0],
        [0, 0]
    ];

    for (let i = 0; i <2; j++){//vai repitir minha linha 45
        for (let j = 0; j <2; j++){// vai repitir minha linha 46
            for(let k = 0; k <2; k++){
                resultado[i][j] += matriz3[i][k] * matriz4[k][j];
            }
        }
    }
    return resultado;
}
const matriz3 = [
    [1, 2],
    [3, 4]
  ];
  
  const matriz4 = [
    [5, 6],
    [7, 8]
  ];

  const resultado = multiplicarMatrizes(matriz3, matriz4);
  console.log("Resultado da multiplicação:");
  console.table(resultado);

  /////4 jogo da velha ta no teste.js pq que não ta pronto
  const {read} = require (`fs`);
const readline = require (`readline`);
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
const tabuleiro = [
  ["", "", ""],//[0, 1 ,2] minha matriz
  ["", "", ""],//[0, 1 ,2]
  ["", "", ""]//[0, 1 ,2]
];

// oq vai aparecer no tabuleiro
function exibirTabuleiro() {
  console.log(tabuleiro.map(row => row.join(" | ")).join("\n---------\n"));// o (" | ") serve pra separa pra ficar visivel no trabuleiro /// ("\n---------\n") cria uma separação visual
}

function verificarVencedor() {// vai me informar ser tem um vencedor ou deu velha
  // Verifica linhas, colunas e diagonais
  for (let i = 0; i < 3; i++) {
      if (tabuleiro[i][0] === tabuleiro[i][1] && tabuleiro[i][1] === tabuleiro[i][2] && tabuleiro[i][0] !== "") {
          return tabuleiro[i][0]; // Linha vencedora
      }
      if (tabuleiro[0][i] === tabuleiro[1][i] && tabuleiro[1][i] === tabuleiro[2][i] && tabuleiro[0][i] !== "") {
          return tabuleiro[0][i]; // Coluna vencedora
      }
  }
  if (tabuleiro[0][0] === tabuleiro[1][1] && tabuleiro[1][1] === tabuleiro[2][2] && tabuleiro[0][0] !== "") {
      return tabuleiro[0][0]; // Diagonal principal
  }
  if (tabuleiro[0][2] === tabuleiro[1][1] && tabuleiro[1][1] === tabuleiro[2][0] && tabuleiro[0][2] !== "") {
      return tabuleiro[0][2]; // Diagonal secundária
  }
  return null; // Sem vencedor
}

// Função principal para jogar o jogo
function jogar() {
  let jogadorAtual = "X";
  let jogadas = 0;

  while (jogadas < 9) {
      exibirTabuleiro();
      rl.question(`Jogador ${jogadorAtual}, escolha a linha (0, 1 ou 2):`)
        rl.question(`Jogador ${jogadorAtual}, escolha a coluna (0, 1 ou 2):`);

      if (tabuleiro[linha][coluna] === "") {
          tabuleiro[linha][coluna] = jogadorAtual;
          jogadas++;

          const vencedor = verificarVencedor();
          if (vencedor) {
              exibirTabuleiro();
              console.log(`Parabéns, jogador ${vencedor}! Você venceu!`);
              return;
          }

          jogadorAtual = jogadorAtual === "X" ? "O" : "X";
      } else {
          console.log("Essa posição já está ocupada. Escolha outra.");
      }
  }

  exibirTabuleiro();
  console.log("Empate! O jogo terminou sem um vencedor.");
}

// Executa o jogo
jogar();

  /////5
  function buscarNumero(matriz, numero) {
    for (let i = 0; i < matriz.length; i++) { // vai repetir pelas linhas da matriz
        for (let j = 0; j < matriz[i].length; j++) { // vai repetir pelas colunas da linha
            if (matriz[i][j] === numero) {
                return { linha: i, coluna: j }; // Retorna a posição 
            }
        }
    }
    return null; // Vai me retorna null se o número não for encontrado
}
// exemplo pra teste
const matrizEx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

const numeroProcurado = 5;
const resultado = buscarNumero(matrizEx, numeroProcurado);

if (resultado) {
    console.log(`Número ${numeroProcurado} encontrado na linha ${resultado.linha} e coluna ${resultado.coluna}.`);
} else {
    console.log(`Número ${numeroProcurado} não encontrado na matriz.`);
}

//////////6

function gerarMatrizIdentidade(n) {
    
    const matrizIdentidade = Array(n).fill(0).map(() => Array(n).fill(0));

    for (let i = 0; i < n; i++) {
        matrizIdentidade[i][i] = 1;
    }

    return matrizIdentidade;
}

// Exemplo de uso
const tamanho = 4; // Tamanho da matriz (N)
const matriz = gerarMatrizIdentidade(tamanho);

console.log(`Matriz Identidade ${tamanho}x${tamanho}:`);
console.table(matriz);

///////7

function rotacionarMatriz(matriz) {
    const tamanho = matriz.length;
    const matrizRotacionada = Array(tamanho).fill(0).map(() => Array(tamanho).fill(0));

    for (let i = 0; i < tamanho; i++) {
        for (let j = 0; j < tamanho; j++) {
            matrizRotacionada[j][tamanho - 1 - i] = matriz[i][j];
        }
    }

    return matrizRotacionada;
}

const matrizOriginal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

console.log("Matriz original:");
console.table(matrizOriginal);

const matrizRotacionada = rotacionarMatriz(matrizOriginal);

console.log("Matriz rotacionada 90 graus no sentido horário:");
console.table(matrizRotacionada);

///////8

function somaDasBordas(matriz) {
    const n = matriz.length;
    let soma = 0;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (i === 0 || i === n - 1 || j === 0 || j === n - 1) {
                soma += matriz[i][j];
            }
        }
    }

    return soma;
}
const matrizExemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

console.log(`Matriz original:`);
console.table(matrizExemplo);

const resultado = somaDasBordas(matrizExemplo);
console.log(`A soma dos elementos das bordas é: ${resultado}`);
