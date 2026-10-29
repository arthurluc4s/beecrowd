#Média 3

nota = list(map(float, input().split()))

peso = [2, 3, 4, 1]

soma = 0.0

for i in range(4):
    soma += (nota[i] * peso[i])

media = soma / 10

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif 5.0 <= media and media <= 6.9:
    exame = float(input())
    final = (media + exame) / 2
    
    print("Aluno em exame.")  
    print(f"Nota do exame: {exame:.1f}")

    if final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print(f"Media final: {final:.1f}")
