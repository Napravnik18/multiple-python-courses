veri = lambda x: 'Par' if x % 2 == 0 else 'impar'

user_num = int(input('Digite um numero: '))
print(f'O numero {user_num} é {veri(user_num)}')