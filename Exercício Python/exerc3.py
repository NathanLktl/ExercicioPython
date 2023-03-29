print("Responda 'Sim' ou 'Não' para as perguntas abaixo:")
print("Digite as palavras da maneira que elas estão escritas acima")
pergunta1 = input("Telefonou para a vítima? ")
pergunta2 = input("Esteve no local do crime? ")
pergunta3 = input("Mora perto da vítima? ")
pergunta4 = input("Devia para a vítima? ")
pergunta5 = input("Já trabalhou com a vítima? ")

if pergunta1 == "Sim" and pergunta2 == "Sim" and pergunta3 == "Sim":
    print("Você é o principal suspeito do crime.")
elif pergunta4 == "Sim":
    print("Você é um suspeito do crime.")
elif pergunta5 == "Sim":
    print("Você é um suspeito do crime.")
else:
    print("Você não é suspeito do crime.")
