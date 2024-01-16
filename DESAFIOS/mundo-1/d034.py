sal = float(input('Digite o salário: '))
if sal <= 1250:
    au = sal * 0.15
    sal = sal + au
    print(f'O salário vai aumentar em R${au:.2f}, ficando agora em R${sal:.2f}.')
else:
    au = sal * 0.1
    sal = sal + au
    print(f'O salário vai aumentar em R${au:.2f}, ficando agora em R${sal:.2f}.')
print('------FIM------')
