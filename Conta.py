class Conta:
    def __init__(self, numero_conta, titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0
    
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        else:
            self.saldo += valor
    
    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        elif valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        else:
            self.saldo -= valor
    
    def obter_saldo(self):
        return self.saldo