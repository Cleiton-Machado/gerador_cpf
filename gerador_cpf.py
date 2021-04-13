from random import randint


def calc(num):  # função interna usada dentro da função digito()
    a = 11 - (num % 11)
    if a > 9:
        a = 0
    return a


def digito(lista_de_numeros_cpf):  # Retorna o dígito do CPF, retorna o 1º se a lista inserida possui 9 dígitos
    # e retorna o 2º se a lista possuir 10 dígitos.
    soma_1 = 0
    for i, v in enumerate(lista_de_numeros_cpf[(len(lista_de_numeros_cpf)) - 1::-1], 2):
        mult = i * v
        soma_1 += mult
    digito = calc(soma_1)
    return digito


cpf = str(randint(000000000, 999999999))
lista = []
for i in cpf:
    if i != '.' and i != '-' and not i.isalpha():
        lista.append(int(i))
lista.append(digito(lista))
lista.append(digito(lista))
for item in lista:
    print(item, end='')
