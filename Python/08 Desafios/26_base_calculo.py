
def calculo(base, expoente=2):
    return base ** expoente

num1 = int(input('Coloque a base '))
num2 = input('Coloque o expoente ')

if num2:
    print(f'O resultado é: {calculo(num1, int(num2))}')
else:
    print(f'O resultado é: {calculo(num1)}')
