#Derivada de Polinômios

while True:
    try:
        t = int(input())
        polinomio = list(map(str, input().split(" + ")))

        size = len(polinomio)

        for i in range(size):
            c, e = map(int, polinomio[i].split("x"))
            
            c *= e
            e -= 1
            if e == 1:
                print(f"{c}x", end="")
            else:
                print(f"{c}x{e}", end="")

            if i == size - 1:
                print()
            else:
                print(" + ", end="")

    except EOFError:
        break