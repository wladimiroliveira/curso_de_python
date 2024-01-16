# DESAFIO 6 -> Crie um programa que leia um número e mostre na tela o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
print(f'O dobro de \033[34m{n}\033[m é \033[32m{n*2}\033[m \nO triplo de \033[34m{n}\033[m é \033[32m{n*3}\033[m \nA raiz quadrada '
      f'de \033[34m{n}\033[m é \033[32m{n**(1/2)}\033[m')
