salario = float(input('Digite o valor do seu salário em reais: '))
aumento = salario + (salario * 0.15)
print('Seu salário irá sofrer um aumento de 15%, portanto passará de R$ {:.2f} para R$ {:.2f}'.format(salario, aumento))
