# DESAFIO 15 -> Escreva um programa que pergunte a quantidade de Km percorridas por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

km = float(input('\nQuantos quilômetros foram rodados com o carro? '))
d = int(input('Quantos dias o carro foi alugado? '))
pkm = 0.15
pd = 60
r = (pkm*km)+(pd*d)
print(f'\nVocê rodou {km:.1f}km, durante {d} dias, sua conta é de R${r:.2f}.\n')
