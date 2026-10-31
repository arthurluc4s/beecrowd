#Tempo de Jogo

i, f = map(int, input().split())

time = 24 - i + f

if i < f:
    time = f - i

print(f"O JOGO DUROU {time} HORA(S)")