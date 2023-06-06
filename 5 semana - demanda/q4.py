class Animal:
    def __init__(self, nome, idade, animal):
        self.nome = nome
        self.idade = idade
        self.animal = animal
    
    def som_info(self):
        if (self.animal).upper() == "CACHORRO":
            return ("AUAUAUUAUAUAUAUA")
        elif (self.animal).upper() == "GATO":
            return ("MIAU")
        elif (self.animal).upper() == "VACA":
            return ("MUUUU")
        else:
            return ("ANIMAL ALÉM DO CÓDIGO FEITO!")