import numpy as np

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

a = sigmoid(0)
b = sigmoid(50)
c = sigmoid(-13)

print(a)
print(b)
print(c)