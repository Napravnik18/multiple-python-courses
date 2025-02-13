

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) #Union = unifica as listas tirando valores repetidos
print(num1 - num2) #Difference = mostra o item que tem na num1 mas não tem na num2
print(num1 ^ num2) #Simmetric Difference = tira os duplicados nas duas listas
print(num1 & num2) #And = o que é duplicado em uma lista e na outra
