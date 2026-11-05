#Há Muito, Muito Tempo Atrás

n = int(input())
i = 0

while i < n:
    ano = int(input())

    ano = 2015 - ano

    if ano <= 0:
        print(f"{abs(ano) + 1} A.C.")
    else:
        print(f"{ano} D.C.")

    i += 1