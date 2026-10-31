#Tipos de Triângulos

a, b, c = map(float, input().split())

if b > a and b > c:
    aux = a
    a = b
    b = aux 
elif c > a and c > b:
    aux = a
    a = c
    c = aux

if c > b:
    aux = b
    b = c
    c = aux 

if a >= b + c:
    
    print("NAO FORMA TRIANGULO")

else:
    if (a ** 2) == (b ** 2 + c ** 2):
        print("TRIANGULO RETANGULO")
    elif (a ** 2) > (b ** 2 + c ** 2):
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES")