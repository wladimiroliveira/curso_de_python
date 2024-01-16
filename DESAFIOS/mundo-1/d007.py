# DESAFIO 7 -> Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'A média do aluno é \033[1;7;32m {m:.2f} \033[m')
