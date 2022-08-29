num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opçao = 0
while opçao != 5:
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NUMEROS
[ 5 ] SAIR DO PROGRAMA''')
    opçao = int(input('Qual a sua opção?: '))
    if opçao == 1:
        soma = num1 + num2
        print('A soma de {} e {} é {}'.format(num1, num2, soma))
    elif opçao == 2:
        multiplicar = num1 * num2
        print('O resultado de {} * {} é {}'.format(num1, num2, multiplicar))
    elif opçao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre {} e {} o maior é {}'.format(num1, num2, maior))
    elif opçao == 4:
        print('Digite os novos números')
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    elif opçao == 5:
        print('Finalizando...')
    else:
        print('Favor digitar um comando valido: ')

print('Fim do programa!')