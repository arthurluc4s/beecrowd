#Médias Ponderadas
n = int(input())
i = 0

while i < n:
    a, b, c = map(float, input().split())

    med = (2 * a + 3 * b + 5 * c) / 10.0

    print(f"{med:.1f}")

    i += 1