velo = int(input('Digite a velocidade do carro em Km/h: '))
if velo > 80:
    multa = (velo - 80) * 7
    print(f'Você foi multado no valor de R${multa:.2f} por excesso de velocidade. ')
else:
    print('Muito bem continue dentro da lei!')
print('------FIM------')
