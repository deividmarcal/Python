produto = float(input('Digite o preço do produto em reais: '))
desconto = produto - (produto * 0.05)
print('Com desconto de 5% o produto passara de R$ {:.2f} para R$ {:.2f}'.format(produto, desconto))
