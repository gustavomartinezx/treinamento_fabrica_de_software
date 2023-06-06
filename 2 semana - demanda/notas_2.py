nota1 = float(input("Insira a sua primeira nota: "))
nota2 = float(input("Insira a sua segunda nota: "))
media = (nota1+ nota2)/2

if media < 5:
    print("REPROVADO! Sua média foi {}".format(media))
elif media >= 5 and media <= 6.9:
    print("RECUPERAÇÃO! Sua média foi {}".format(media))
else:
    print("APROVADO! Sua média foi {}".format(media))