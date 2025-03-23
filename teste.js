const tabuleiro = [
  ["", "", ""],
  ["", "", ""],
  ["", "", ""]
];

// oq vai aparecer no tabuleiro
function exibirTabuleiro() {
  console.log(tabuleiro.map(row => row.join(" | ")).join("\n---------\n"));
}

// Fverificar se há um vencedor
function verificarVencedor() {
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
      const linha = prompt(`Jogador ${jogadorAtual}, escolha a linha (0, 1 ou 2):`);
      const coluna = prompt(`Jogador ${jogadorAtual}, escolha a coluna (0, 1 ou 2):`);

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