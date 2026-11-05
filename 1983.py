#O Escolhido
n = int(input())

i = 0
nota_max = 0.0
inscricao_max = 0

while i < n:
    
    inscricao, nota = input().split()

    inscricao = int(inscricao)
    nota = float(nota)

    if(nota >= 8.0 and nota_max < nota):
        nota_max = nota
        inscricao_max = inscricao

    i += 1

if nota_max > 0:
    print(inscricao_max)
else:
    print("Minimum note not reached")
