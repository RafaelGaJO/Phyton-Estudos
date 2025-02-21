resp = "sim"
while resp.lower() == "sim":

    print("-----olimpiadas de paris-----")
    a = input("digiteo nome do atleta : ")
    b1 = float(input("digite a nota do atleta : "))
    print("-----olimpiadas de paris-----")
    c = input("digiteo nome do atleta : ")
    d2 = float(input("digite a nota do atleta : "))
    print("-----olimpiadas de paris-----")
    e = input("digiteo nome do atleta : ")
    f3 = float(input("digite a nota do atleta : "))

    if b1 > d2 and d2>f3:
        print(a,"ouro")
        print(e,"prata")
        print(c,"bronze")
    
    elif b1 > f3 and f3> d2:
        print(a,"ouro")
        print(c,"prata")
        print(e,"bronze")
    
    elif d2> b1 and b1 > f3:
        print(c,"ouro")
        print(a,"prata")
        print(e,"bronze")
    
    elif d2>f3 and f3 >b1:
        print(c,"ouro")
        print(e,"prata")
        print(a,"bronze")

    elif f3>d2 and d2>b1:
        print(e,"ouro")
        print(c,"prata")
        print(a,"bronze")
    
    elif f3>b1 and b1 > d2:
        print(e,"ouro")
        print(a,"prata")
        print(c,"bronze")

    resp= input("quer continuar?")
    



        


