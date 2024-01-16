nome = ' Wladimir '
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[1;7;40m'}
print('Olá, seja muito bem vindo(a) {} !!!'.format(cores['pretobranco'] + nome + cores['limpa']))
