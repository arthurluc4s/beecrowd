#Xadrez

l = int(input())
c = int(input())

cor = 0

if l % 2 == 0:
    if c % 2 == 0:
        cor = 1
else:
    if c % 2 != 0:
        cor = 1

print(f"{cor}")