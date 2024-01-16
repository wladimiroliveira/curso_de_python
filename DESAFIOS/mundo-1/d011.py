#DESAFIO 11 -> Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

l = float(input('\nEm metros digite a largura da parede: '))
a = float(input('Em metros digite a altura da parede: '))
ap = float(input('Quantos metros quadrados se pinta com 1 litro da tinta? '))
ar = l*a
li = ar/ap
print(f'\nVocê precisará de {li:.2f} litros de tinta para pintar a parede.\n')
