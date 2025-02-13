
paises = {'Brasil': 'Brasilia', 'Bolivia': 'Sucre', 'Chile': 'Santiago', 'Equador': 'Quito', 'Peru': 'Lima'}

guess_usuario = input('digite um país: ')
if guess_usuario in paises:
    print(f'a capital do país {guess_usuario} é {paises[guess_usuario]}')
else:
    print('Desculpe, não temos informações sobre a capital deste país')