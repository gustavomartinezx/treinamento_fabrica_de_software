def contador():
    inicio = int(input("Insira o inicio do seu contador: "))
    fim = int(input("insira o fim do seu contador: "))
    passo = int(input("insira o passo do seu contador: "))
    
    escolha = input("""Escolha um passo:
    a) 1 até 10, de 1 em 1
    b) de 10 até 1, de 2 em 2
    c) contador personalizado
    """).upper()

    if escolha == "A":
        for x in range(1, 10):
            print(x) 
    elif escolha == "B":
        for x in range(0, 10):
            print(10-x)
    elif escolha == "C":
        for x in range(inicio, fim, passo):
            print(x)
    
contador()