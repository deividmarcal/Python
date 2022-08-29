somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range (1,5):
    print('--- {}ª PESSOA ---'.format(c))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip().upper()
    somaidade += idade
    if c == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1

media = somaidade / 4
print('A media de idade é {}'.format(media))
print('O homem mais velho tem {} anos e seu nome é {}'.format(maioridadehomem, nomevelho))
print('{} mulheres tem menos de 20 anos'.format(totmulher20))
