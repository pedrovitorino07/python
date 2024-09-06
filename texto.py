faturamento = 1000
custo = 700

lucro = faturamento - custo

# print(f"Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}") # f"faturamento : pode adicionar uma variavel a uma string
# print("Faturamento: " + str(faturamento) + ", Custo: " + str(custo) + ", Lucro: "+ str(lucro)) # + : concatena textos // str() : adiciona uma variavel, similar ao ${} do js

email = "email_falso@gmail.com"

print(email.lower()) #.lower(), função de texto que deixa tudo em minusculo
print(email.find("@")) #.find(), procura um caractere especifico na string e retorna sua posição na string // -1 -> caso não encontre o elemento

posicao = email.find("@") # string[] -> retorna o caractere correspondente ao numero dentro do colchetes
servidor = email[posicao+1:] # string[posicao:] -> retorna do caractere especifico para trás // string[:posicao] -> retorna do caractere especifico pra frente
#string[posicao+1:] -> pula o caractere correspondente ao numero e mostra o resto
print(servidor)
