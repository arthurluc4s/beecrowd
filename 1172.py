#Substituição em Vetor I

x = []

n = 10

for i in range(n):
    valor = int(input())

    if(valor <= 0):
        valor = 1

    x.append(valor)

    print(f"X[{i}] = {x[i]}")