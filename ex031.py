dist = float(input('Digite a distancia em Km da viagem: '))
if dist <=200:
    preço = dist * 0.50
    print('O preço da viagem será R$ {:.2f}'.format(preço))
else:
    preço2 = dist * 0.45
    print('O preço da viagem será R$ {:.2f}'.format(preço2))