def area(h, largura):
    resultado = h * largura 
    print( "A área do terreno é {}".format(resultado) )

altura = int(input("Insira a altura do terreno: "))
largura = int(input("Insira a largura do terreno: "))

area(altura, largura)