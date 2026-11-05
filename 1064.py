#Positivos e Média
i = 0
soma = 0
positivos = 0

while i < 6:
    n = float(input())

    if n > 0:
        positivos += 1
        soma += n
    
    i += 1

med = soma / positivos

print(f"{positivos} valores positivos")
print(f"{med:.1f}")