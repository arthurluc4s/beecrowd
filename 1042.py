#Sort Simples

a, b, c = map(int, input().split())

a1 = a
b1 = b
c1 = c

if a < b and a < c and b > c:
    b1 = c        
    c1 = b    
if b < a and b < c:
    a1 = b
    if a < c:
        b1 = a
        c1 = c
    else:
        b1 = c        
        c1 = a
elif c < a and c < b:
    a1 = c
    if a < b:
        b1 = a
        c1 = b
    else:
        b1 = b
        c1 = a

print(f"{a1}\n{b1}\n{c1}\n")

print(f"{a}\n{b}\n{c}")