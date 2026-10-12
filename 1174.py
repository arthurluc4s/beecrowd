#Seleçao em Vetor I

a = []
n = 100

for i in range(n):
    val = float(input())
    a.append(val)
    if(a[i] <= 10):
        print(f"A[{i}] = {a[i]:.1f}")