#Zero vale Zero

m, n = map(int, input().split())

while m != 0 or n != 0:

    soma = str(m + n)

    for i in range(len(soma)):
        if soma[i] != '0':
            print(soma[i], end="")

    print()  

    m, n = map(int, input().split())