//
let nome = "João";
let idade1 = 25;
console.log(nome, idade1);

//

let a = 10;
let b = 5;
console.log("Soma:", a + b);
console.log("Subtração:", a - b);
console.log("Multiplicação:", a * b);
console.log("Divisão:", a / b);

//

let primeiroNome = "Maria";
let sobrenome = "Silva";
let nomeCompleto = primeiroNome + " " + sobrenome;
console.log(nomeCompleto);

//

let x = 15;
let y = 20;
console.log("x é maior que y?", x > y);
console.log("x é igual a y?", x === y);

//

let temCarteira = true;
let idade = 18;
let temCarro = false;
let podeDirigir = idade >= 18 || temCarteira;
console.log("Pode dirigir?", podeDirigir);
console.log("Pode dirigir e tem carro?", podeDirigir && temCarro);

//

let frase = "JavaScript é divertido";
console.log(frase.toUpperCase());
let novaFrase = frase.replace("divertido", "poderoso");
console.log(novaFrase);

//

let contador = 0;
contador += 5; //contador=contador+5
contador -= 2; //contador=contador-2
contador *= 3; //contador=contador*3
console.log("Valor final do contador:", contador);