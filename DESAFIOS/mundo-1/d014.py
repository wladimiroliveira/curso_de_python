# DESAFIO 14 -> Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

cel = float(input('\nDigite a temperatura em °C: '))
far = (cel * 1.8) + 32
print(f'A temperatura de {cel:.1f}°C convertida para °F é = {far:.1f}°F\n')
