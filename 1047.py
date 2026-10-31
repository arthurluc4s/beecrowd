#Tempo de Jogo com Minutos

hi, mi, hf, mf = map(int, input().split())

h = 24 - hi + hf
m = mf - mi

if mi == mf and hi < hf:
    h = hf - hi
elif mi > mf:
    h -= 1
    m = 60 - mi + mf
    if hi < hf:
        h = hf - hi - 1
elif mi < mf and hi <= hf:
        h = hf - hi

print(f"O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)")