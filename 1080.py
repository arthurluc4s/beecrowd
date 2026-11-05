#Maior e Posição
i = 1
maior = 0
posicao = 0

while i <= 100:
    n = int(input())

    if i == 1:
        maior = n
        posicao = 1

    if maior < n:
        maior = n
        posicao = i
    
    i += 1

print(maior)
print(posicao)