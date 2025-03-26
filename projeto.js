class Aluno {
    constructor(nome, matricula, curso) {
        this.nome = nome;
        this.matricula = matricula;
        this.curso = curso;
        this.notas = [];
    }

    adicionarNota(nota) {
        this.notas.push(nota);
    }

    calcularMedia() {
        if (this.notas.length === 0) {
            return 0;
        }
        const soma = this.notas.reduce((acc, nota) => acc + nota, 0);
        return soma / this.notas.length;
    }
}

// teste pra ver ser ta funcionado
const aluno1 = new Aluno("Maria", "20250123", "Computação");
aluno1.adicionarNota(8);
aluno1.adicionarNota(9);
aluno1.adicionarNota(7);

console.log(`Nome: ${aluno1.nome}`);
console.log(`Média: ${aluno1.calcularMedia().toFixed(2)}`);