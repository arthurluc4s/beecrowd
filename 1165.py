#Nome do problema: Número Primo

def eh_primo(n):
    if(n == 2):
        return True
    if(n < 2 or n % 2 == 0):
        return False

    limite = int(n ** 0.5)
    
    for i in range(3, limite + 1, 2):
        if(n % i == 0):
            return False
    
    return True

n = int(input())

for i in range(n):
    numero = int(input())

    if(eh_primo(numero)):
        print(f"{numero} eh primo")
    else:
        print(f"{numero} nao eh primo")