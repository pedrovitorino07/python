precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

dic_precos = {"celular": 1500, "camera": 1000, "fone de ouvido":800, "monitor": 2000}

# pegar um item
preco_celular = dic_precos["celular"]
print(preco_celular)

# atualiza valor de um item do dicionario
dic_precos["camera"] = 2000
print(dic_precos)

# quando não existe item no dicionario, e tenta editar ele adiciona no dicionario
dic_precos["iphone"] = 4500
print(dic_precos)

dic_precos.pop("iphone")
print(dic_precos)

