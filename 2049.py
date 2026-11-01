#Números de Ahmoc

a = int(input())
count = 1

while a != 0:
    if(count > 1):
        print("")

    ass = list(str(a))
    painel = list(input().strip())

    size_p = len(painel)
    size_a = len(ass)
    encontrou = False

    for i in range(size_p - size_a + 1):    
        
        num_iguais = 0
        
        for j in range(size_a):
            
            if painel[i + j] == ass[j]:
                num_iguais += 1
            else:
                break

        if num_iguais == size_a:
            encontrou = True
            break

    print(f"Instancia {count}")
    
    if encontrou:
        print("verdadeira")
    else:
        print("falsa")

    a = int(input())

    count += 1