
try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em numeros')

finally:
    print('codigo ok')


'''
else:
    print('Usuario digitou valor valido')
    resultado = valor * 3
    print(resultado)
'''