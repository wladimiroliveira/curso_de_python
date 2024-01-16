# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um
# programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
alunos = input('\nDigite o nome dos alunos: ')
alunos = alunos.split()
random.shuffle(alunos)
print(f'A ordem de entrega do trabalho é a seguinte » {alunos}')
# PRONTO
