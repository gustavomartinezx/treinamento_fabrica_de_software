num1 = int(input("Insira o 1° número: "))
num2 = int(input("Insira o 2° número: "))
num3 = int(input("Insira o 3° número: "))

if num1 == num2 and num2 == num3:
    print("Dois iguais e um diferente")
elif num1 == num2 and num1 != num3:
    print("Dois iguais e um diferente")
elif num1 != num2 and num1 == num3:
    print("Dois iguais e um diferente")
elif num2 != num1 and num2 == num3:
    print("Dois iguais e um diferente")
elif num2 == num1 and num2 != num3:
    print("Dois iguais e um diferente")
elif num3 != num1 and num3 == num2:
    print("Dois iguais e um diferente")
elif num3 == num1 and num3 != num2:
    print("Dois iguais e um diferente")
elif num1 != num2 and num1 != num3 and num2 != num3:
    print("Três diferentes")