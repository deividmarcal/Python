n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 6:
    print('Parabéns sua média foi de {}, portanto você foi aprovado'.format(media))
else:
    print('Sinto muito, sua média foi de {}, portanto você está reprovado'.format(media))