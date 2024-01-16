import random
frase = 'Curso em Vídeo Python'
palavra = input('Digite uma palavra para substituir Vídeo: ')
frase = frase.replace('Vídeo', palavra)
letra = input('Busque uma letra: ')
print(frase)
print(f'A letra ({letra}) aparece {frase.count(letra)} vezes dentro da frase.')
spalavra = input('Procure uma palavra: ')
print(f'A palavra ({spalavra}) esta dentro da frase? {spalavra in frase}, '
      f'e ela aparece a partir do item número {frase.find(spalavra)}')
frase = frase.split()
print(frase)
random.shuffle(frase)
frase = ' '.join(frase)
print(f'A frase embaralhada fica da seguinte maneira: \n{frase}')
