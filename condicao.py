# faturamento = 1000
# custo = 1800

# lucro = faturamento - custo

# if lucro >= 0:
#     print("Lucro:",lucro)
# else:
#     print("Prejuizo!")
#     print(lucro)

# produtos = ["iphone", "ipad", "airpod"]
# novo_produto = input("Digite aqui o produto:")
# novo_produto = novo_produto.lower() # trata o novo produto em minusculo pra n dar bigode

# if novo_produto in produtos:
#     print("Este produto já cadastrado!")
# else:
#     print("Produto cadastrado com sucesso!")
#     produtos.append(novo_produto) # adicionar produto a lista

# print(produtos)

# acima de 15000 -> 500 de bonus
# acima de 10000 -> 150 de bonus
# acima de 5000 -> 50 de bonus
vendas = 10000

if vendas > 15000:
    bonus = 500
elif vendas > 10000:
    bonus = 150
elif vendas > 5000:
    bonus = 50
else:
    bonus = 0
    
print("Bonus:", bonus)

if vendas > 5000:
    if vendas > 10000:
       if vendas > 15000: 
           bonus = 500
       else:
         bonus = 150
    else:   
        bonus = 50
else:
    bonus = 0
    
print("Bonus:", bonus)