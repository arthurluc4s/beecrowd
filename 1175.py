#Troca em Vetor I

size = 20
n = []

for i in range(size):
    valor = int(input())
    n.append(valor)

for j in range(size // 2):
    #Define elemento anterior x e elemento posterior y
    x = j
    y = -(j+1)

    #Troca elementos
    aux = n[x]
    n[x] = n[y]
    n[y] = aux

for k in range(size):
    print(f"N[{k}] = {n[k]}")