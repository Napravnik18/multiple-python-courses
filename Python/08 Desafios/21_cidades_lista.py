
cidades = ['São Paulo', 'Fortaleza', 'Salvador']
guess_usuario = input('Digite o nome da cidade: ')

if guess_usuario in cidades:
    print('A cidade está na lista')
else:
    print('A cidade não está na lista')