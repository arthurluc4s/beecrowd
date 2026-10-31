#Animal

str1 = input()
str2 = input()
str3 = input()

if str1 == "vertebrado":
    if str2 == "ave":
        if str3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if str3 == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if str2 == "inseto":
        if str3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if str3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
