class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade 
        self.salario = salario

    def funcionario_info(self):
        return ("O funcionário {} do salário {} tem o aumento de R$1500, ficando com o {}")