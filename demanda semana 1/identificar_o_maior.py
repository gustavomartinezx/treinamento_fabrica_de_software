num1 = int(input("Insira o 1° número: "))
num2 = int(input("Insira o 2° número: "))
num3 = int(input("Insira o 3° número: "))
num4 = int(input("Insira o 4° número: "))
num5 = int(input("Insira o 5° número: "))

if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
    print("O maior número é o: " , num1)
elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5:
    print("O maior número é o: " , num2)
elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
    print("O maior número é o: " , num3)
elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
    print("O maior número é o: " , num4)
elif num5 >= num1 and num5 >= num2 and num5 >= num3 and num5 >= num4:
    print("O maior número é o: ", num5)