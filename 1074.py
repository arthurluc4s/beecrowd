#Par ou Ímpar

n = int(input())
i = 0

while i < n:
    num = int(input())

    if num % 2 == 0:
        if num < 0:
            print("EVEN NEGATIVE")
        elif num > 0:
            print("EVEN POSITIVE")
        else:
            print("NULL")
    else:
        if num < 0:
            print("ODD NEGATIVE")
        else:
            print("ODD POSITIVE")
   
    i += 1