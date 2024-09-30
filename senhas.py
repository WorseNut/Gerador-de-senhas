import random

print('Gerador de senhas')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&?'

number = input('Quantidade de senhas a serem geradas: ')
number = int(number)

length = input('Insira o tamanho da sua senha: ')
length = int(length)

print('\nAqui estão suas senhas:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
