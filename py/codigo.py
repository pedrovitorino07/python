faturamento = 1200 # numero inteiro -> int
custo = 770

novas_vendas = 300
faturamento = faturamento + novas_vendas

taxas_imposto = 0.1 # numero decimal -> float
mensagem = "O faturamento foi de " # string = texto
teve_lucro = False # boolean 

imposto = taxas_imposto * faturamento
print("Faturamento", faturamento)
print("Custo", custo)
print("Lucro", faturamento - custo - imposto)
print(mensagem, faturamento)