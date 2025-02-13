
def soma(*numeros):
    result = 0
    for num in numeros:
        result += num
    return result

x= soma(2,3,4,7)

print(x)