
// 1: Crie uma função que recebe um array de números e retorna
//a soma de todos os elementos.
function soma(array){
return array.reduce((acc,num) => acc + num,0);
}
    let num = [1,2,3,4,5];
    let resultado = soma(num);
    console.log(`a soma é ${resultado}`);









// 2: Crie uma função que recebe um array de strings e retorna um
//novo array com as strings em ordem alfabética.
function ordenarStrings(arr) {
    return arr.sort();
}

let frutas2 = ["Banana", "Maçã", "Laranja", "Abacaxi"];
console.log("Frutas ordenadas:", ordenarStrings(frutas2));





// 3: Crie uma função que recebe um array e retorna um novo array
// sem elementos duplicados.	
function removerDuplicados(arr) {
    return [...new Set(arr)];
}

let numeros3 = [1, 2, 2, 3, 4, 4, 5];
console.log("Sem duplicados:", removerDuplicados(numeros3));