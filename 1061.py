#Tempo de um Evento

_, d1 = input().split()
h1, m1, s1 = map(int, input().split(" : "))

_, d2 = input().split()
h2, m2, s2 = map(int, input().split(" : "))

d1 = int(d1)
d2 = int(d2)

t1 = s1 + (60 * m1) + (h1 * 3600) + (d1 * 3600 * 24)
t2 = s2 + (60 * m2) + (h2 * 3600) + (d2 * 3600 * 24)

dt = t2 - t1

d = dt // (3600 * 24)

dt %= (3600 * 24)

h = dt // 3600

dt %= 3600

m = dt // 60

s = dt % 60

print(f"{d} dia(s)")
print(f"{h} hora(s)")
print(f"{m} minuto(s)")
print(f"{s} segundo(s)")