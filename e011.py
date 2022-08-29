altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
m2 = altura * largura
pintar = m2 / 2
print('A parede tem {} m2, e serão necessários {:.2f} litros para pinta-lá'.format(m2, pintar))