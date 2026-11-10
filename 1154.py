#Idades

idade = int(input())

n = 0
soma = 0

while idade > 0:
    soma += idade

    n += 1
    
    idade = int(input())

media = 0

if soma > 0:
    media = soma / n


print(f"{media:.2f}")