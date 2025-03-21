//vetores em javaScrip são estruturas de dados que permitem armazenar muitas variaveis
let frutas = ["maçã", "banana", "laranja"];//pra vc chamar os itens começa por (0,1,2,3...)ou seja ser eu chamar apenas a banana vai seguir a ordem [maça=0,banana=1,laranja=2]
console.log(frutas);// vai ficar console.log(frutas [1]) no termial vai aparecer "banana"
//
frutas.push("laranja");//comando do python (push) pra enpurar uma variavel    DE UMA FORMA MAS FORMAL, adicona um ou mais elementos
console.log(fruntas);
//
console.log(frutas.length);//não temos uma função cont diretamente
//
let copiafrutas = frutas.slice();//fazer uma copia pra fazer teste no seu codigo, ser der erro só a copia vai ser danificado
console.log(copiafrutas);
//
let randomIndex = math.floor(Math.random() * frutas.length); // comando de uma biblioteca chamada random,pra fazer um elemento aleatorio tipo um bing
console.log(frutaa[randomIndex]);
//
function range (start,end){
    return Array.from({length:end - start + 1},(_,i) => start + i); //range não é copilada igual do python ,no js tem que criar esse codigo
}
//
let num= [3,1,4,1,5,9];
num.sort((a,b) => a - b);//comando pra colocar em ordem paraordernado ou seja color em orde alfabetica ou numerica
console.log(num);
//
let numeros = [5,3,8,1,9];
numeros.sort((a,b) => a - b);
console.log("ordenado:",numeros)

let randomNum = numero[Math.floor(Math.random() * numeros.length)];
console.log("numero de elementos:",randomNum);
//contar um numero de elementos 
console.log("Numeros de elementos",numeros.length);