//2

// Declarar as classes 
class Professor {
    constructor(nome, departamento) {// O construtor da classe recebe dois parâmetros: 'nome' e 'departamento'.
        this.nome = nome;//atribui o nome do professor 
        this.departamento = departamento;
        this.disciplinas = [];
        this.turmas = []; 
    }

    // Atribuir uma disciplina
    atribuirDisciplina(disciplina) {
        if (!this.disciplinas.includes(disciplina)) {
            this.disciplinas.push(disciplina);
            console.log(`Disciplina ${disciplina} atribuída ao professor ${this.nome}.`);
        } else {
            console.log(`Professor ${this.nome} já ministra a disciplina ${disciplina}.`);
        }
    }

    // Listar as disciplinas atribuídas
    listarDisciplina() {
        if (this.disciplinas.length > 0) {
            console.log(`O professor ${this.nome} ministra as seguintes disciplinas:`);
            this.disciplinas.forEach(disciplina => console.log(`- ${disciplina}`));
        } else {
            console.log(`Professor ${this.nome} ainda não tem disciplinas atribuídas.`);
        }
    }

    // Listar as turmas atribuídas
    listarTurmas() {
        if (this.turmas.length === 0) {
            console.log(`${this.nome} ainda não tem turmas atribuídas.`);
        } else {
            console.log(`Turmas atribuídas ao professor ${this.nome}:`);
            this.turmas.forEach((turma, index) => {
                console.log(`${index + 1}. ${turma}`);
            });
        }
    }

    // Método para atribuir turma 
    atribuirTurma(turma) {
        if (!this.turmas.includes(turma)) {
            this.turmas.push(turma);
            console.log(`Turma ${turma} atribuída ao professor ${this.nome}.`);
        } else {
            console.log(`Professor ${this.nome} já tem a turma ${turma} atribuída.`);
        }
    }
}


const professor1 = new Professor("Carlos Silva", "Matemática");
const professor2 = new Professor("joão","fisica");

// Atribuindo disciplinas
professor1.atribuirDisciplina("Ciências");
professor1.atribuirDisciplina("Matemática");
professor2.atribuirDisciplina("ed fisica");
professor2.atribuirDisciplina("fisica");

// Atribuindo turmas
professor1.atribuirTurma("Turma A - 2009");
professor1.atribuirTurma("Turma B - 2010");
professor2.atribuirTurma("turma c - 2011");
professor2.atribuirTurma("turma d - 2012");
// Listando disciplinas e turmas
professor1.listarDisciplina();
professor1.listarTurmas();
professor2.listarDisciplina();
professor2.listarTurmas();