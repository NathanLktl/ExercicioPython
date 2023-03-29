def encontrar_primos(n):
    numeros = list(range(1, n+1))
    
    for i in range(2, int(n**0.5)+1):
        if numeros[i-1] != 0:
            for j in range(i**2, n+1, i):
                numeros[j-1] = 0

    return [x for x in numeros if x != 0 and x != 1]
    
n = int(input("Digite um número inteiro N: "))

primos = encontrar_primos(n)

print("Os números primos entre 1 e", n, "são:", primos)
