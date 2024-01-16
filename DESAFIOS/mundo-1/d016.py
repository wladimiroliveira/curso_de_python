# DESAFIO 16 > Crie um programa que leia um número Real qualquer pelo teclado, e mostre na tela a sua porção
# inteira. EX: Digite um número: 6.127 O número 6.127 tem a parte inteira 6.
from math import trunc
num = float(input('\nDigite um número real qualquer: '))
iNum = trunc(num)
print(f'A parte inteira do número {num} é {iNum}')
# PRONTO
