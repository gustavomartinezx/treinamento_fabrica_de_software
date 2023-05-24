from q13 import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, idade, emprego):
        super().__init__(nome, idade)
        self.emprego = emprego
    
    def aumentar_salario(self):
        self.salario = self.salario + 1500