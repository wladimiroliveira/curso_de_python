l1 = float(input('Linha 1: '))
l2 = float(input('Linha 2: '))
l3 = float(input('Linha 3: '))
if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    print('As três linhas podem formar um triângulo.')
else:
    print('As três linhas não podem formar um triângulo.')
print('------FIM------')
