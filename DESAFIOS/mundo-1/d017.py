# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
from math import hypot
a = float(input('\nDigite o comprimento do primeiro cateto: '))
b = float(input('Digite o comprimento do segundo cateto: '))
c = hypot(a, b)
print(f'\nEm relação aos catetos A = {a} e B = {b}, temos que o comprimento da hipotenusa é = {c:.2f}\n')
# PRONTO
