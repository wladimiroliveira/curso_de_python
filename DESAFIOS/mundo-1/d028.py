from random import randint
from time import sleep
n = randint(0, 5)
print('-=-' * 15)
print('Estou pensando em um número entre 0 e 5...')
print('-=-' * 15)
chute = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if chute == n:
    print('Parabéns! Você acertou!')
elif chute > 5:
    print('Não, escolha um número entre 0 e 5, reinicie o programa e tente de novo.')
else:
    print(f'Que pena, você errou, o número que eu pensei foi {n}.')
