#Resto da Divisão

x = int(input())
y = int(input())

if x > y:
    aux = x
    x = y
    y = aux

while x < y:

    x += 1
    resto = x % 5

    if resto == 2 or resto == 3:
        print(x)