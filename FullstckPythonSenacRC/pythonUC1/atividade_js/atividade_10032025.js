//Cálculo de Desconto em uma Loja Declare duas variáveis, preco e desconto, com valores 150.0 e 20, respectivamente. Calcule o preço final após aplicar o desconto e imprima o resultado.
let preco = 150.0;
let desconto = 20;
console.log(preco-desconto);


//Cálculo de IMC (Índice de Massa Corporal) Declare duas variáveis, peso e altura, com valores 70 e 1.75, respectivamente. Calcule o IMC usando a fórmula: IMC = peso / (altura ** 2). Imprima o resultado.
let peso = 70;
let altura = 1.75;
let imc=peso /(altura **2)
console.log(imc)


//Verificação de Elegibilidade para um Concurso Declare duas variáveis, idade e tem_experiencia, com valores 22 e True, respectivamente. Verifique se a pessoa é elegível para o concurso (idade maior ou igual a 18 e tem experiência) e imprima o resultado.

let tem_experiencia = true;
let idade = 22;
let idade_maior = idade >=18 && tem_experiencia;
console.log("tem experiencia", idade_maior);

//Classificação de Níveis de Acesso Declare uma variável nivel_acesso com um valor entre 1 e 3. Use estruturas condicionais para imprimir:
//"Acesso total" se o nível for 3. "Acesso parcial" se o nível for 2. "Acesso restrito" se o nível for 1

let nivel_acesso =3
if (nivel_acesso === 3) {
    console.log("Acesso total");
}else if (nivel_acesso <3) {
    console.log("Acesso parcial");
}else if (nivel_acesso <2) { 
    console.log("Acesso restrito")
    }else { (nivel_acesso >3) 
    console.log("numero invalido");
}    


//Conversão de Temperatura Declare uma variável celsius com um valor de temperatura em graus Celsius. Converta a temperatura para Fahrenheit usando a fórmula: F = (C * 9/5) + 32. Imprima o resultado.

let c = 94;
let f =(c * 9/5) + 32;
console.log("a temperatura é",f);

//Verificação de Números Pares e Ímpares Declare uma variável numero com um valor inteiro. Use estruturas condicionais para verificar se o número é par ou ímpar e imprima o resultado.
let numero = 7;
if (numero % 2 === 0) {
    console.log("O número é par");
} else {
    console.log("O número é ímpar");
}

//Cálculo de Frete com Base no Peso Declare uma variável peso com o peso de um pacote em kg. Calcule o frete com base nas seguintes regras

let peso2 = 8;
let frete;
if (peso2 <= 5) {
    frete = 10; //
}else if (peso2 > 5 && peso2 <= 10) {
    frete = 20;
}else {
        frete = 30; // Frete para pacotes acima de 10 kg
    }
    console.log("O valor do frete é: R$ " + frete);