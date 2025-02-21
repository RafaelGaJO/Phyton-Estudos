
import random


b = random.randint(1000, 9999)

while True:
    a = input("Digite uma senha de no máximo 4 dígitos: ")
    if not a.isdigit():
        print("Entrada inválida. Digite apenas números.")
        continue
    a = int(a)
    if 1000 <= a <= 9999:
        if a == b:
            print("Acertou!")
            break
        else:
            print("Tente novamente.")
    else:
        print("Digite um número de 4 dígitos.")

print("Fim do jogo!")



