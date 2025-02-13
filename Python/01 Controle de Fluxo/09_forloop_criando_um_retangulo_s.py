

linhas = 1
colunas = 6
simbolo = 'O'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end=' ')
    print()
    print(simbolo,'       ', simbolo)
    print(simbolo,'       ', simbolo)
    print(simbolo,'       ', simbolo)
    print(simbolo,'       ', simbolo)
    print(simbolo,'       ', simbolo)
    for c in range(colunas):
        print(simbolo, end=' ')
    print()