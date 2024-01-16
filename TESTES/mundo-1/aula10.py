n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2
print(f'A sua média foi de {m:.1f}.')
print('Sua média foi boa!') if m >= 6 else print('Você deixou a desejar!')
'''if m >= 6.0:
    print('Sua média foi boa. PARABÉNS!')
else:
    print('Você deixou a desejar. ESTUDE MAIS!')'''
