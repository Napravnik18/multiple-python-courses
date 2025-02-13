
frutas = ['maçã', 'banana', 'pessego', 'maçã', 'jamba', 'maçã', 'tomate']
contador = 0

for fruta in frutas:
    if fruta == 'maçã':
        contador += 1
        
print(f'existem {contador} maçãs na lista')