#Menor e Posição

n = int(input())
x = list(map(int, input().split()))

menor = x[0]
idx = 0

for i in range(n):
    if(x[i] < menor):
        menor = x[i]
        idx = i

print(f"Menor valor: {menor}\nPosicao: {idx}")