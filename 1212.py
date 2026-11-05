#Aritmética Primária

a, b = map(int, input().split())

while a != 0 or b != 0:
    carry = 0
    count_carry = 0

    while a != 0 or b != 0 or carry != 0:
        digit_a = a % 10
        digit_b = b % 10

        carry = (digit_a + digit_b + carry) // 10
        count_carry += carry

        a = a // 10
        b = b // 10

    if count_carry == 0:
        print("No carry operation.")
    elif count_carry == 1:
        print(f"{count_carry} carry operation.")
    else:
        print(f"{count_carry} carry operations.")

    a, b = map(int, input().split())