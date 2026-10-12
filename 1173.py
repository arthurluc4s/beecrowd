#Preenchimento de Vetor I

n = 10
val = int(input())
v = []

for i in range(n):
    if i == 0:
        v.append(val) 
    else: 
        dobro = v[i-1] * 2
        v.append(dobro)
    
    print(f"N[{i}] = {v[i]}")