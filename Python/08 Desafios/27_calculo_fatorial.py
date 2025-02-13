def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
user_number = int(input('digite um numero: '))
print(f'O fatorial de {user_number} é {fatorial(user_number)}')