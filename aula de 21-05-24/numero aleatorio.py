
import random
b= random.randint(1000,9999)
a= 6666
while a!=b:
 a= int(input("digite uma senha de no maximo 4 digitos : "))
 if a==b:
  print("acertou!!!!!")
 elif a < 1000 or a > 9999:
  print(" caractere invalido")
 else:
  print("tente novamente")