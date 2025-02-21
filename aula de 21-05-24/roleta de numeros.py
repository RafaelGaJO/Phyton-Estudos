import random
b=random.randint(0,10)
a=1230
while b!=a:
    a=int(input("tente acertar um numero de 0 a 10 : "))
    if a==b:
        print("você acertou")
    else:
        print("tente novamente")