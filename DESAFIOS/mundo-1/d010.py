# DESAFIO 10 -> Crie um programa que leia quanto a dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere: US$1,00 = R$4,87

d = float(input('\nDigite o valor que você tem na carteira: '))
do = 4.87
eu = 5.34
rd = d/do
re = d/eu
print(f'Com o seu dinheiro (R${d:.2f}), você pode comprar US${rd:.2f} ou EUR${re:.2f}.\n')
