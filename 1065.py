#Pares entre Cinco Números

i = 1
pares = 0

while i <= 5:
    num = int(input())

    if num % 2 == 0:
        pares += 1

    i += 1

print(f"{pares} valores pares")