casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do salário: '))
anos = int(input('Quantos anos de financiamento?: '))
prestação = (casa / anos) / 12
if prestação > salario * 0.3:
    print('Emprestimo negado')
else:
    print('Emprestimo consedido')
