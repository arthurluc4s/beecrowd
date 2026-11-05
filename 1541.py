#Construindo Casas
import math

linha = input().split()

while linha[0] > '0':

    a, b, c = map(int, linha)

    area = (a * b * 100) / c
    
    lado = int(math.sqrt(area))
    
    print(lado)

    linha = input().split()