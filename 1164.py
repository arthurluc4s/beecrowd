#Número Perfeito

n = int(input())
i = 0

while i < n:
    
    valor = int(input())
    count = 1
    soma_divisores = 0
    
    while count < valor:
        if valor % count == 0:
            soma_divisores += count
        
        count += 1
        
    if soma_divisores == valor:
        print(f"{valor} eh perfeito")
    else:
        print(f"{valor} nao eh perfeito")

    i += 1