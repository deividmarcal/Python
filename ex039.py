from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade < 18:
    faltam = 18 - idade
    alistamento = atual + faltam
    print('Ainda faltam {} anos para seu alistamento, seu alistamento será em {}'.format(faltam, alistamento))
elif idade == 18:
    print('Você deve se alistar esse ano')
elif idade > 18:
    passou = idade - 18
    alistamento = atual - passou
    print('O alistamento deveria ter sido feito {} anos atras, em {}'.format(passou, alistamento))



