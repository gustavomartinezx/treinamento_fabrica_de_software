class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_info(self):
        return ("O ser {} tem {} anos".format(self.nome, self.idade))