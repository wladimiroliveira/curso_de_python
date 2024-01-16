# Um professor quer sortear um dos alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e
# escrevendo o nome escolhido.
from random import choice
n1 = input('Digite o nome do primeiro aluno(a): ')
n2 = input('Digite o nome do segundo aluno(a): ')
n3 = input('Digite o nome do terceiro aluno(a): ')
n4 = input('Digite o nome do quarto aluno(a): ')
print(f'\nO aluno(a) escolhido para limpar o quadro foi {choice([n1, n2, n3, n4])}')
# PRONTO
