#Sequência Espelho

n = int(input())

for i in range(n):
    b, e = map(int, input().split())

    #Vai
    for j in range(b,e + 1):
        print(j, end="")

    for j in range(e, b - 1, -1):
        
        numero = j

        while numero > 0:
            digit = numero % 10          
            
            print(digit, end="")

            numero //= 10

    print(end="\n")