distance = int(input('Digite a distância da viagem em Km: '))
if distance <= 200:
    p = distance * 0.5
    print(f'A passagem para uma viagem de {distance}Km custará R${p:.2f}.')
else:
    p = distance * 0.45
    print(f'A passagem para uma viagem de {distance}Km custará R${p:.2f}.')
print('------FIM------')
