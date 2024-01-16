# DESAFIO 8 -> Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('\nDigite um valor em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print(f'\nO valor \033[35m{m}m\033[m, convertido para km é = \033[32m{km:.3f}km\033[m.')
print(f'O valor \033[35m{m}m\033[m, convertido para hectômetro é = \033[32m{hm:.3f}hm\033[m.')
print(f'O valor \033[35m{m}m\033[m, convertido para decâmetros é = \033[32m{dam:.3f}dam\033[m.')
print(f'O valor \033[35m{m}m\033[m, convertido para decímetros é = \033[32m{dm:.0f}dm\033[m.')
print(f'O valor \033[35m{m}m\033[m, convertido para centímetros é = \033[32m{cm:.0f}cm\033[m.')
print(f'O valor \033[35m{m}m\033[m, convertido para milímetros é = \033[32m{mm:.0f}mm\033[m.\n')
