#Fuso Horário

s, t, f = map(int, input().split())

print(f"{(s + t + f) % 24}")