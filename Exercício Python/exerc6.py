n = int(input("Digite um número inteiro: "))

resultado = 1

for i in range(1, n+1):
    resultado *= i

print(f"O fatorial de {n} é: {resultado}")
