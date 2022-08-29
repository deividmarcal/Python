salario = float(input('Digite seu salário: R$  '))
if salario > 1250:
    aumento = salario + (salario * 0.1)
    print('Seu salário irá aumentar 10%, portanto passará a ser R$ {:.2f}'.format(aumento))
else:
    aumento2 = salario + (salario * 0.15)
    print('Seu salário irá aumentar 15%, portando passará a ser R$ {:.2f}'.format(aumento2))

