# DESAFIO 13 -> Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('\nDigite o salário: '))
a = float(input('Digite a porcentagem do aumento: '))
au = a*0.01
r = s + (s*au)
print(f'\nO salário de R${s:.2f} com um aumento de {a:.2f}%, ficou R${r:.2f}\n')
