
carros_estoque = ['BMW X6', 'BMW i5', 'BMW i8']
cliente_search = input('Que carro deseja comprar? ')

if cliente_search in carros_estoque:
    print('Em estoque')
else:
    print('No hay papito')