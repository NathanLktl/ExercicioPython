numero = int(input("Digite um número de 1 a 10 para gerar sua tabuada: "))

if numero < 1 or numero > 10:
    print("Número inválido!")
else:
    print("Tabuada do número", numero)
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)
