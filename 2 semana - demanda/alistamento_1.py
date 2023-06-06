nascimento = int(input("Insira a ano de nascimento: "))
idade = 2023 - nascimento

if idade < 18:
    print("Você ainda irá se alistar! Falta {} anos para o seu alistamento".format(18-idade))
elif idade == 18:
    print("Você tem que se alistar")
else:
    print("Já passou da hora de se alistar! Já passou {} anos do seu alistamento".format(idade - 18))