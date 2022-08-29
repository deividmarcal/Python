ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
decimo = ptermo + (10-1) * razao
for c in range (ptermo, decimo, razao):
    print('{}'.format(c), end= ' -> ')
print('FIM')
