import random
pcescolha = (random.randint(0,5))
escolha = int(input('Digite um número de 1 a 5: '))
if pcescolha == escolha:
    print('Parabens, você ganhou')
elif pcescolha != escolha:
    print('Você perdeu, eu havia escolhido o numero {}'.format(pcescolha))
