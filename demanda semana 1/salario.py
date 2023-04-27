salario = float(input("Insira o seu salário: R$"))
gastos = float(input("Insira os seus gastos: R$"))

if salario - gastos >= 0:
    print("Dentro do orçamento! Saldo de R$", salario - gastos)
else:
    print("Fora do orçamento! Saldo devedor de R$", salario -gastos)