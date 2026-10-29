#Lanche

cod, qtd = map(int, input().split())

t = float(qtd)

if cod == 1:
    t *= 4.0
elif cod == 2:
    t *= 4.5
elif cod == 3:
    t *= 5.0
elif cod == 4:
    t *= 2.0
elif cod == 5:
    t *= 1.5

print(f"Total: R$ {t:.2f}")