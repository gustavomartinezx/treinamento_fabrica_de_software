nasc = int(input("Em que ano você nasceu? "))
idade = 2023 - nasc

if idade < 18:
    print("Menor de idade, tendo ", idade, " anos")
else:
    print("Maior de idade, tendo ", idade, " anos")