num = (input('Digite um número de 0 a 9999: '))

if len(num) == 4:
    print(f'Unidade: {num[3]}')
    print(f'Dezena: {num[2]}')
    print(f'Centena: {num[1]}')
    print(f'Milhar: {num[0]}')
elif len(num) == 3:
    print(f'Unidade: {num[2]}')
    print(f'Dezena: {num[1]}')
    print(f'Centena: {num[0]}')
elif len(num) == 2:
    print(f'Unidade: {num[1]}')
    print(f'Dezena: {num[0]}')
else:
    print(f'Unidade: {num[0]}')
