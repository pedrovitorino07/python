produtos = ["iphone", "ipad", "airpode"]

while True:
    novo_produto = input("Digite aqui o produto: ")
    novo_produto = novo_produto.lower() # trata o novo produto em minusculo pra n dar bigode
    
    if "sair" == novo_produto:
        break
    
    if novo_produto in produtos:
        print("Este produto já cadastrado!")
        
    else:
        print("Produto cadastrado com sucesso!")
        produtos.append(novo_produto)

print(produtos)