precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

dic_precos = {"celular": 1500, "camera": 1000, 
              "fone de ouvido": 800, "monitor": 2000 }

# pegar um item
preco_celular = dic_precos["celular"]
print(preco_celular)

dic_precos["celular"] = 2000
print(dic_precos)

dic_precos["iphone"] = 4500
print(dic_precos)

# exclui um item do dicionario
dic_precos.pop("iphone")
print(dic_precos)

# tamanho do dicionario
print(len(dic_precos))

# printa as chaves
print(dic_precos.keys())

# printa os valores
print(dic_precos.values())

# exercicio 

produto_procurado = input("digite um produto:")
produto_procurado = produto_procurado.lower()

if produto_procurado in dic_precos:
    preco = dic_precos[produto_procurado]
    print(f"Produto {produto_procurado}, Preço: {preco}")
else:
    print("produto não encontrado!")