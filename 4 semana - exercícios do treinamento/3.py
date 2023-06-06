def escreva(texto):
    tam = len(texto)
    print ("-" * tam)
    print(f'{texto}')
    print ("-" * tam)

text = str(input("Insira o texto formatado: "))

escreva(text)