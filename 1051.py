#Imposto de Renda

sal = float(input())

sal -= 2000.00
ir = 0.00

if sal > 0:
    if sal > 1000:
        ir += 1000 * 0.08
        sal -= 1000.00

        if sal > 1500:
            ir += 1500 * 0.18
            sal -= 1500.00
            ir += sal * 0.28
        else:
            ir += sal * 0.18
    else:
        ir += sal * 0.08

    print(f"R$ {ir:.2f}")
else:
    print("Isento")