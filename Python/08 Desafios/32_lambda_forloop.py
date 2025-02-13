numeros = [2, 4, 5, 6, 9]
quadrado = lambda x: x ** 2

resultados = []
for numero in numeros:
    resultados.append(quadrado(numero))
    
print(resultados)