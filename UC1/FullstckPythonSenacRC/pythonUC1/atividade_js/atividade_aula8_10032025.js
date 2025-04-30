const { read } = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function notas(nota1, nota2, nota3, nota4) {
    let medianotas = (nota1 + nota2 + nota3 + nota4) / 4;

    if (medianotas >= 7) {
        return "Aprovado";
    } else if (medianotas >= 5 && medianotas < 7) {
        return "Recuperação";
    } else {
        return "Reprovado";
    }
}

rl.question("Digite a primeira nota:", (nota1) => {
    rl.question("Digite a segunda nota:", (nota2) => {
        rl.question("Digite a terceira nota:", (nota3) => {
            rl.question("Digite a quarta nota:", (nota4) => {
                nota1 = parseFloat(nota1);
                nota2 = parseFloat(nota2);
                nota3 = parseFloat(nota3);
                nota4 = parseFloat(nota4);

                let resultado = notas(nota1, nota2, nota3, nota4);
                console.log("Classificação das notas: ", resultado);

                rl.close();
            });
        });
    })
});
//
const readline = require('readline');

// interface para ler entradas e saídas
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Função para calcular a soma dos números pares em um intervalo
function somaNumerosPares(inicio, fim) {
    let soma = 0;
    
    // Percorre o intervalo de início até o fim
    for (let i = inicio; i <= fim; i++) {
        // Verifica se o número é par
        if (i % 2 === 0) { //%=a modulo não percentual
            soma += i;
        }
    }

    // Retorna a soma
    return soma;
}

// Pergunta ao usuário o número de início e fim do intervalo
rl.question("Digite o número de início do intervalo: ", (inicio) => {
    rl.question("Digite o número de fim do intervalo: ", (fim) => {
        // Converte as entradas em números inteiros
        const inicioNum = parseInt(inicio);
        const fimNum = parseInt(fim);

        // Chama a função e exibe o resultado
        const resultado = somaNumerosPares(inicioNum, fimNum);
        console.log(`A soma dos números pares no intervalo de ${inicioNum} a ${fimNum} é: ${resultado}`);

        // Fecha a interface de leitura
        rl.close();
    });
});
//
function verificarPalidromo(){
    let textoInformado = texto.replace(/ /g,"").toLowerCase()
    const textoReverso = textoInformado.split("").reversr().join("");
    if ( texto === textoReverso){
        console.log("É palindromo");
    }else {
        console.log("Nãp é um palindromo");
    }
}
//
function calculorjurosimples(){
    let p= parseFloat(input("Digite o valor principal (P): "));
    let r = parseFloat(input("Digite a taxa de juros anual (r) em decimal (por exemplo, 0.05 para 5%): "));
    let t = parseFloat(input("Digite o tempo em anos (t): "));
    let M = P * (1 + r * t);
    console.log("montante final:",M);
}
//
function contarDigitos() {
    let numero = prompt ("digite um número inteiro positivo:");
    if (/^\d+$/.test(numero) ) {// isdigit(um teste pra não acabar com seu coidado codigo)GRAVAR***(/^\d+$/.test(variavel))
        console.log("número de digitos:",numero.length);
    } else{
        console.log("entrada iválida.Digite um número inteiro positivo");
    }
}
//
