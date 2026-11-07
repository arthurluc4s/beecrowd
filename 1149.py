#Somando Inteiros Consecutivos

linha = input().split()

idx = len(linha) - 1
n = int(linha[idx])

a = -1
idx = 0
while a <= 0:
    valor = int(linha[idx])
    
    if valor > 0:
        a = valor

soma = 0
i = 0
while i <= n - 1:
    soma += a + i
    
    i += 1

print(soma)