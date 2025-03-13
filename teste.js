let peso = 8;
let frete;
if (peso <= 5) {
    frete = 20;
} else if (peso > 5 && peso <= 10) {
    frete = 35;
} else {
        frete = 50; // Frete para pacotes acima de 10 kg
    }
    console.log("O valor do frete é: R$ " + frete);