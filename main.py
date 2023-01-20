from random import randint

saldo = 20
seguidas = 0
variavel = 1

while True:
    aposta = randint(0,1)
    if aposta == 0:
        aposta = 'Falso'
    else:
        aposta = 'Verdadeiro'

    usuario = input('Qual a sua aposta? ').capitalize().strip() # falso ou verdadeiro

    if aposta == usuario:
        print('Parabéns, você acertou!')
        saldo = saldo + variavel
        seguidas = 0
    else:
        print('VOCÊ ERROU!')
        saldo = saldo - variavel
        seguidas = seguidas + 1
    
    if seguidas == 0:
        variavel = 1
    if seguidas == 1:
        variavel = 3
    if seguidas == 2:
        variavel = 8
    
    if saldo <= 0:
        print('PARABÉNS, SEU INÚTIL! VOCÊ CONSEGUIU PERDER TUDO!!!')
        break
    elif saldo >= 40:
        print('Parabéns, você conseguiu faturar 20 reais, malucooo!!')
        break
    else:
        print(f'Seu saldo é: R${saldo}\n')
