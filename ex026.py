frase = str(input('Digite uma frase: ')).strip()
fupper = frase.upper()
print('A letra A aparece {} vezes'.format(fupper.count('A')))
print('A primeira letra A aparece na posição {}'.format(fupper.find('A')+1))
print('A ultima letra A aparece na posição {}'.format(fupper.rfind('A')))