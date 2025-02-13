
produtos = ['arroz', 'feijão', 'laranja', 'banana', 'carne', 'frango', 'pamonha']
#             0         1         2           3        4        5          6

item1, item2,*outros, item3, = produtos

print(item1)
print(item2)
print(item3)
print(outros)