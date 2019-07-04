from random import randint
numero= int(randint(0,10))
palp = 0
ponto = 0
while palp != numero:
    palp = int(input('Digite um palpite:'))
    ponto += 1
    if palp == numero:
        print('Acertou!! seu placar é: {}'.format(ponto))
    elif palp < numero:
        print('Tente um numero maior')
    else:
        print('Chute um valor menor')
print('Fim de jogo!')
