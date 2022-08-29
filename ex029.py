vel = float(input('Digite a velocidade do carro: '))
if vel <= 80:
    print('Você estava dentro do limite de velocidade.')
elif vel > 80:
    multa = (vel - 80)  * 7
    print('Multado, sua velocidade estava superior ao permitido, você pagara uma multa de R$ {:.2f}'.format(multa))
