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

# tamanho de um texto
tamanho = len(email)
print(tamanho)

# trocar um pedaço de texto
email_trocado = email.replace("gmail.com", "hotmail.com")
print(email_trocado)

nome = "pedro vitorino"
print(nome.capitalize()) # deixa a primeira letra maiuscula
print(nome.title()) # deixa a primeira letra de cada palavra maiuscula

# especiais
margem = lucro / faturamento           
print(f"Faturamento: R${faturamento:,.2f}\n Custo: {custo}\n Lucro: {lucro}")
print(f"Margem: {margem:.1%}")

# exercícios
nome2 = "Pedro Lucas Vitorino"
email2 = "pedrofalso@gmail.com"

# descubra o servidor do email

posicao2 = email2.find("@")
servidor2 = email2[posicao2+1:]
print(servidor2)

# pegar o 1° nome do usuário

posicao2espaço = nome2.find(" ") # procura o espaço entre um nome e outro
primerionome = nome2[:posicao2espaço]
print(primerionome)

# construa uma mensagem: usuario pedro cadastrado com sucesso com o email tal

print(f"Usuario {primerionome} cadastrado com sucesso com o email {email2}!")

# construa uma mengasem: enviamos um link de confirmação para o email p***@gmail.com

primeiraletra = email2[0] # retorna quem está no indice 0 ou o primeiro caractere da string
print(f"Enviamos um link de confirmacoo para o email {primeiraletra}***{servidor}!")