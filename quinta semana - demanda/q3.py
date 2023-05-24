class ContaBancaria:
    def __init__(self, titular, num_conta, saldo):
        self.titular = titular
        self.num_conta = num_conta
        self.saldo = saldo
    
    def depositar(self, dinheiro):
        self.saldo = int(self.saldo) + int(dinheiro)
    
    def sacar(self, dinheiro):
        self.saldo = int(self.saldo) - int(dinheiro)

    def saldo_info(self):
        return self.saldo