#Desafio de Bino

i = 0
n = int(input())
num = list(map(int, input().split()))

m2 = 0
m3 = 0
m4 = 0
m5 = 0

while i < n:
    if num[i] % 2 == 0:
       m2 += 1 
    if num[i] % 3 == 0:
        m3 += 1
    if num[i] % 4 == 0:
        m4 += 1
    if num[i] % 5 == 0:
        m5 += 1

    i += 1

print(f"{m2} Multiplo(s) de 2")
print(f"{m3} Multiplo(s) de 3")
print(f"{m4} Multiplo(s) de 4")
print(f"{m5} Multiplo(s) de 5")