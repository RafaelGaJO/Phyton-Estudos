import random

vetor = []

while len(vetor) < 6:
    numeroAleatorio = random.randint(0,6)
    vetor.append(numeroAleatorio)

for i in range (6):
    for y in range (6):
        if vetor[i] == vetor[y]:
            numeroAleatorio = random.randint(0,6)
            vetor.append(numeroAleatorio)
print(vetor)