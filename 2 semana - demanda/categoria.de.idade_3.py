nascimento = int(input("Insira seu ano de nascimento: "))
idade = 2023 - nascimento

if idade <= 9:
    print("Categoria: MIRIM")
elif idade > 9 and idade <= 14:
    print("Categoria: INFANTIL")
elif idade > 14 and idade <= 19:
    print("Categoria: JUNIOR")
elif idade == 20:
    print("Categoria: SÊNIOR")
else:
    print("Categoria: MASTER")