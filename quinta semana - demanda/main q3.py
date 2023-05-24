from q3 import ContaBancaria

conta = ContaBancaria("Gustavo", "1031", 100)
conta.depositar(100)
conta.sacar(200)
print(conta.saldo_info())