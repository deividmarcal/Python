from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    data = int(input('Digite o ano de nascimento da pessoa {}ª. '.format(c)))
    idade = atual - data
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas menores de idade.'.format(totmenor))