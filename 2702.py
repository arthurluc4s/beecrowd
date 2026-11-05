#Escolha Difícil

c0, b0, p0 = map(int, input().split())
c1, b1, p1 = map(int, input().split())

m = 0

if c0 < c1:
    m += c1 - c0

if b0 < b1:
    m += b1 - b0

if p0 < p1:
    m += p1 - p0

print("{}".format(m))