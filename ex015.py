km = float(input('Digite a quantidade de Km percorridos: '))
dias = int(input('Digite a quantidade de dias pelos quais o carro foi alugado: '))
preçokm = km * 0.15
preçodia = dias * 60
preçototal = preçokm + preçodia
print('O total a pagar é {}'.format(preçototal))