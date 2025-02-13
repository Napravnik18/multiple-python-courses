def dobro(num1):
    return num1 * 2

def quadrado(num1):
    return dobro(num1) ** 2

numero = int(input('Digite um numero: '))

print(f'o quadrado do dobro de {numero} é {quadrado(numero)}')
