const readline = require('readline');

const rl = readline.createinfece({
    input: process.stdin,
    output: process.stdout
})

function calcularIMC(nota1, nota2 , nota3 , nota4){
    let media= (nota1 + nota2 + nota3 + nota4)/4;
    if (media >=7){
        return "aprovado";
    }else if (media >=4){
        return "recuperação";
    }else "reprovado"