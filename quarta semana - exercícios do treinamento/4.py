def maior():
    tamanho = int(input("Insira a quantidade de termos à serem escritos: "))

    for b in range(1, tamanho+1):

        valor = int(input("Insira um valor: "))

        if b == 1:
            maior = valor
        elif b != 1 and b!= tamanho:
            if valor >= maior:
                maior = valor
        elif b == tamanho:
            print("O maior é {}".format(maior))

maior()
        