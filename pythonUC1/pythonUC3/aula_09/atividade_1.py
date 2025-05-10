class ContaBancária:
    def __init__(self, saldo_inicial=0):
        """Inicializa a conta com um saldo inicial."""
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        """Retorna o saldo formatado como moeda (R$1.000,00)."""
        return f"R${self._saldo:,.2f}".replace(",", "@").replace(".", ",").replace("@", ".")

    @saldo.setter
    def saldo(self, valor):
        """Impede valores negativos e atualiza saldo."""
        if valor < 0:
            raise ValueError("Erro: O saldo não pode ser negativo!")
        self._saldo = valor

    def depositar(self, valor):
        """Adiciona dinheiro à conta."""
        if valor <= 0:
            print("Erro: O valor do depósito deve ser positivo.")
            return
        self._saldo += valor
        print(f"Depósito de R${valor:,.2f} realizado com sucesso!")

    def sacar(self, valor):
        """Retira dinheiro, garantindo que não fique com saldo negativo."""
        if valor > self._saldo:
            print("Erro: Saldo insuficiente!")
            return
        self._saldo -= valor
        print(f"Saque de R${valor:,.2f} realizado com sucesso!")

# Teste:
conta = ContaBancária(1500)
print(conta.saldo)  # Saída: R$1.500,00

conta.depositar(500)
print(conta.saldo)  # Saída: R$2.000,00

conta.sacar(750)
print(conta.saldo)  # Saída: R$1.250,00

conta.saldo = -100  # ERRO! Gera ValueError
