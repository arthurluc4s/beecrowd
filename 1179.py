#Preenchimento de Vetor IV

n = 15

par = []
impar = []

i_par = 0
i_impar = 0

for i in range(n):
    val = int(input())

    if(val % 2 == 0):
        par.append(val)
        i_par += 1
        if(i_par == 5):
            for j in range(5):
                print(f"par[{j}] = {par[j]}")

            par = []
            i_par = 0
    else:
        impar.append(val)
        i_impar += 1
        if(i_impar == 5):
            for j in range(5):
                print(f"impar[{j}] = {impar[j]}")

            impar = []
            i_impar = 0

for i in range(i_impar):
    print(f"impar[{i}] = {impar[i]}")

for i in range(i_par):
    print(f"par[{i}] = {par[i]}")