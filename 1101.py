#Sequência de Números e Soma

m, n = map(int, input().split())

while m > 0 and n > 0:

    if m > n:
        aux = m
        m = n
        n = aux

    sum = 0

    while m <= n:
        print(m, end=" ")
        sum += m
        m += 1

    print(f"Sum={sum}")
    
    m, n = map(int, input().split())