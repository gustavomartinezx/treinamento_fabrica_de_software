frase = input("insira a frase: ")
palavra = input("Insira a palavra que deseja saber se há na string: ")

if frase.count(palavra) >= 1:
    print(True)
else: 
    print(False)