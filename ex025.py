nome = str(input('Digite um nome: ')).strip()
silva = 'SILVA' in nome.upper()
if silva == True:
    print('Sim, existe Silva no nome')
else:
    print('Não existe Silva no nome')