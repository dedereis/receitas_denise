class Banco:
    def __init__(self):
        self.contas = {}
    
    def adicionar_conta(self, conta):
        if conta.numero_conta in self.contas:
            raise ValueError("Já existe uma conta com esse número.")
        else:
            self.contas[conta.numero_conta] = conta
    
    def remover_conta(self, numero_conta):
        if numero_conta in self.contas:
            del self.contas[numero_conta]
        else:
            raise ValueError("Não existe uma conta com esse número.")
    
    def listar_contas(self):
        return list(self.contas.values())