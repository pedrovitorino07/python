vendas = [100, 50, 130, 80, 120, 200] 

print(vendas[-1]) # devolve o indice correspondente // -1 retorna o ultimo indice

total_vendas = sum(vendas) #soma todos os indices da lista
print(total_vendas)
quantidade = len(vendas) #conta quantos indices tem na lista
print(quantidade)
valor_max = max(vendas) #pega o maior valor da listaa
valor_min = min(vendas) #pega o menor valor da list
print(valor_max, valor_min)

posicao = vendas.index(130) # retorna a posição de um indice na lista
print(posicao)
print(vendas[2:])

produtos = ["iphone", "ipad", "airpod"]
precos = [4000, 8000, 2000]

print("iphone" in produtos) # verifica se oq foi digitado no input tem na lista
novo_preco = precos[0] * 1.1
precos[0] = novo_preco # edita um valor da lista
print(precos)

produtos.append("macbook") # add um item pra lista
precos.append(10000)
print(produtos)
print(precos)

# remove um item da lista
produtos.remove("macbook") #remove pelo valor
precos.pop(-1) # remove pela posição
print(produtos)
print(precos)

# inserir um valor
produtos.insert(1, "airpod") # insere o item num indice especifico
print(produtos)

# contar valores
print(produtos.count("airpod")) #conta os valores especificos

# ordenar lista
precos.sort(reverse=True) # ordena em ordem decrescente
precos.sort() # ordena em ordem crescente
print(precos)
