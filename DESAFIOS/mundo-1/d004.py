# DESAFIO 4 = Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele
cores = {
    'limpo': '\033[m',
    'vdd': '\033[1;7;32m',
    'fal': '\033[1;7;31m'
}
t = input('\nDigite algo: ')

print(f'\nO tipo primitivo desse item é {type(t)}')
print(f'O item só tem espaços? {cores['vdd']} {t.isspace()} {cores['limpo']}') if t.isspace() == True \
    else print(f'O item só tem espaços? {cores['fal']} {t.isspace()} {cores['limpo']}')
print(f'O item é numérico? {cores['vdd']} {t.isnumeric()} {cores['limpo']}') if t.isnumeric() == True \
    else print(f'O item é numérico? {cores['fal']} {t.isnumeric()} {cores['limpo']}')
print(f'O item é decimal? {cores['vdd']} {t.isdecimal()} {cores['limpo']}') if t.isdecimal() == True \
    else print(f'O item é decimal? {cores['fal']} {t.isdecimal()} {cores['limpo']}')
print(f'O item é alfabético? {cores['vdd']} {t.isalpha()} {cores['limpo']}') if t.isalpha() == True \
    else print(f'O item é alfabético? {cores['fal']} {t.isalpha()} {cores['limpo']}')
print(f'O item é alfanumérico? {cores['vdd']} {t.isalnum()} {cores['limpo']}') if t.isalnum() == True \
    else print(f'O item é alfanumérico? {cores['fal']} {t.isalnum()} {cores['limpo']}')
print(f'O item está todo em maiúsculas? {cores['vdd']} {t.isupper()} {cores['limpo']}') if t.isupper() == True \
    else print(f'O item está todo em maiúsculas? {cores['fal']} {t.isupper()} {cores['limpo']}')
print(f'O item está todo em minúsculas? {cores['vdd']} {t.islower()} {cores['limpo']}') if t.islower() == True \
    else print(f'O item está todo em minúsculas? {cores['fal']} {t.islower()} {cores['limpo']}')
print(f'O item está capitalizado? {cores['vdd']} {t.istitle()} {cores['limpo']}') if t.istitle() == True \
    else print(f'O item está capitalizado? {cores['fal']} {t.istitle()} {cores['limpo']}')
print('True corresponde a verdadeiro, e False corresponde a falso.\n')
'''print(f'\nO tipo primitivo desse item é {type(t)}')
print(f'O item só tem espaços? {cores['vdd']} {t.isspace()}\n')
print(f'O item é numérico? {t.isnumeric()}')
print(f'O item é decimal? {t.isdecimal()}')
print(f'O item é alfabético? {t.isalpha()}')
print(f'O item é alfanumérico? {t.isalnum()}')
print(f'O item está todo em maiúsculas? {t.isupper()}')
print(f'O item está todo em minúsculas? {t.islower()}')
print(f'O item está capitalizado? {t.istitle()}')
print('True corresponde a verdadeiro, e False corresponde a falso.\n')'''
