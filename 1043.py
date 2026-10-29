#Triângulo

a, b, c = map(float, input().split())

#Troca de lugar: o maior é atribuido a a
if b > a and b > c:
    aux = a
    a = b
    b = aux
elif c > a and c > b:
    aux = a
    a = c
    c = aux

if a < (b + c):
    print(f"Perimetro = {a + b + c:.1f}")
else:
    print(f"Area = {(a + b) * c / 2:.1f}")