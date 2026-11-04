
n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    r = (3 * x) ** 2 + y ** 2
    b = 2 * (x ** 2) + (5 * y) ** 2
    c = -100 * x + y ** 3

    if(r > b and r > c):
        print(f"Rafael ganhou")
    elif(b > r and b > c):
        print(f"Beto ganhou")
    else:
        print(f"Carlos ganhou")