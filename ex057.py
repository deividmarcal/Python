sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, por favor digite seu sexo [M/F]: ')).upper().strip()
print ('Sexo {} registrado com sucesso'.format(sexo))