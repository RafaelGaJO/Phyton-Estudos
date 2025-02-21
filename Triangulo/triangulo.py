resp = 'sim'
while resp.lower() == 'sim':

    print("calculadora do triangulo")
    print(" 1-área \n 2-perimetro \n 3-hipotenusa \n 4-angulos internos")

    a=int(input("escolha uma das opçoes : "))
    match a:
        case 1:
            b=float(input("digite a haltura :"))
            c=float(input("digitr a base :")) 
            print( b*c/2)
        case 2 : 
            b=float(input("digite a haltura :"))
            c=float(input("digite a base :"))
            print(b+b+c+c)
        case 3 : 
            d=float(input("digite um cateto :"))
            e=float(input("digite o outro cateto :"))
            hipotenusa = (d ** 2 + e** 2) ** (1/2)
            print("O valor da hipotenusa é: {}".format(hipotenusa))
        
        case 4: 
            f= float(input("digite um angulo interno :"))
            g= float(input("digite um angulo interno :"))
            print(180-(f+g))
    resp=input("deseja continuar? sim ou não : ")

# print("calculadora do triangulo")
# print("1-área \n2-perimetro \n3-hipotenusa \n4-angulos internos")

# a = int(input("escolha uma das opções: "))
# match a:
#     case 1:
#         b = float(input("digite a altura: "))
#         c = float(input("digite a base: ")) 
#         print("A área do triângulo é: {}".format(b * c / 2))
#     case 2:
#         b = float(input("digite a altura: "))
#         c = float(input("digite a base: "))
#         print("O perímetro do triângulo é: {}".format(b + b + c + c))
#     case 3:
#         d = float(input("digite um cateto: "))
#         e = float(input("digite o outro cateto: "))
#         hipotenusa = (d ** 2 + e ** 2) ** (1/2)
#         print("O valor da hipotenusa é: {}".format(hipotenusa))
#     case 4:
#         f = float(input("digite um ângulo interno: "))
#         g = float(input("digite outro ângulo interno: "))
#         print("O valor do terceiro ângulo é: {}".format(180 - (f + g)))