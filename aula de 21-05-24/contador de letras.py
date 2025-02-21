a=input("digite uma frase : ")
b=0
c=0
while c<len(a):
    if a[c]== 'a'or a[c]=='A':
        b+=1
    c+=1
print("a letra a aparece",b,"vezes na frase")