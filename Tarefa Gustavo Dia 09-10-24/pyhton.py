respostaUsuario= "sim"

soma = 0

while respostaUsuario == "sim":
    quantidadeItens= int(input("Digite a quantidade de itens que você vai usar: "))
    for i in range(quantidadeItens):
        nomeItem = input('Digite o nome do item:')
        precoItem = float(input('Digite o preço do item:'))
        soma += precoItem
    
    print('O valor total de investimento é de:', soma , " e foram necessários :" , quantidadeItens , " produtos." )
    respostaUsuario = input('Você deseja fazer novamente? \n (sim) (não)')