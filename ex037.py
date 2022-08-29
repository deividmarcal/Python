num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Digite sua opção: '))
if opção == 1:
    print('O número {} em binário é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} em octal é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Favor selecionar uma das opções acima!')
