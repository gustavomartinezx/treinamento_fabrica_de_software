frase = "Treinamento hoje de backend"
print(frase)
palavra = input("Coloque a palavra que você quer substituir: ")
palavra_sub = input("Coloque a palavra que será a substituta: ")

frase_nova = frase.replace(palavra, palavra_sub)

print("Sua nova frase é : \"", frase_nova, "\"")