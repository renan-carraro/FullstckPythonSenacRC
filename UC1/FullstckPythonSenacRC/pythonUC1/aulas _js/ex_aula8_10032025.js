const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function calcularIMC(peso, altura) {
    let imc = peso / (altura * altura);

    if (imc < 18.5) {
        return "Abaixo do peso";
    } else if (imc >= 18.5 && imc <= 24.9) {
        return "Peso Normal";
    } else if (imc >= 25 && imc <= 29.9) {
        return "Sobrepeso";
    } else if (imc >= 30 && imc <= 34.9) {
        return "Obesidade Grau I";        
    } else if (imc >= 35 && imc <= 39.9) {
        return "Obesidade Grau II";
    } else {
        return "Obesidade Grau III";
    }
}

rl.question("Digite o seu peso: ", (peso) => {
    rl.question("Digite a sua altura: ", (altura) => {
        peso = parseFloat(peso);
        altura = parseFloat(altura);

        let resultado = calcularIMC(peso, altura);
        console.log("Classificação do IMC: ", resultado);

        rl.close();
    });
});
//
AULA 9 - 19/03/2025

function calcularMedia() {
    let soma = 0;
    for (let i = 0; i < 4; i++) {
        let nota = parseFloat(prompt(`Digite a ${i + 1}ª nota:`));
        soma += nota;
    }
    let media = soma / 4;
    console.log("Média:", media);
    if (media >= 7) {
        console.log("Aprovado");
    } else {
        console.log("Reprovado");
    }
}
