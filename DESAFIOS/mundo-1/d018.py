# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
a = int(input('Digite um ângulo qualquer: '))
rad = math.radians(a)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f'Para o ângulo {a} temos as seguintes informações:')
print(f'Seno = {sen:.4f}')
print(f'Cosseno = {cos:.4f}')
print(f'Tangente = {tan:.4f}')
# PRONTO
