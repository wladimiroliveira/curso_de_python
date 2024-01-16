# DESAFIO 12 -> Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('\nDigite o valor do produto: '))
d = float(input('Digite a porcentagem de desconto para este produto: '))
de = d*0.01
r = p - (p*de)
print(f'\nO produto com {d:.2f}% de desconto, sai por R${r:.2f}', '\n')
