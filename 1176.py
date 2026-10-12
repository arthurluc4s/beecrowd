#Fibonacci em Vetor

f = [0, 1]

n_termos = 2

n = int(input())

for i in range(n):
    
    idx = int(input())
    
    if(idx >= n_termos):
        inicio = n_termos
        n_termos = idx + 1

        for i in range(inicio, n_termos):
            f.append(f[i - 1] + f[i - 2])
    
    print(f"Fib({idx}) = {f[idx]}")