
#Aumento de Salário

sal = float(input())

fator = 0

if sal >= 0 and sal <= 400.00:
    fator = 15
elif sal <= 800.00:
    fator = 12
elif sal <= 1200.00:
    fator = 10
elif sal <= 2000.00:
    fator = 7
else:
    fator = 4

if(fator != 0):
    novo = sal * (fator + 100) / 100
else:
    novo = sal

print(f"Novo salario: {novo:.2f}")
print(f"Reajuste ganho: {novo - sal:.2f}")
print(f"Em percentual: {fator} %")