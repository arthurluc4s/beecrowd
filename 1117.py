#Validação de Nota

notas_validas = 0
soma_notas = 0

while notas_validas < 2:

    nota = float(input())

    #Verifica a validade da nota
    if 0 <= nota <= 10:
        notas_validas += 1
        soma_notas += nota
    else:
        print("nota invalida")

med = soma_notas / 2.0

print(f"media = {med:.2f}")