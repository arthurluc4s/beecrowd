#Qual Triângulo

a, b, c = map(int, input().split())

#Atribui o maior valor a A
if b > a and b > c:
    aux = a
    a = b
    b = aux
elif c > a and c > b:
    aux = a
    a = c
    c = aux

if a >= (b + c):
    print("Invalido")
else:
    if a == b and a == c:
        print("Valido-Equilatero")
    elif a == b or a == c or b == c:
        print("Valido-Isoceles")
    else:
        print("Valido-Escaleno")

    if a ** 2 == b ** 2 + c ** 2:
        print("Retangulo: S")
    else: 
        print("Retangulo: N")