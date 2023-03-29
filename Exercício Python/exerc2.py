num = int(input("Digite um número inteiro menor que 1000: "))

if num >= 1000:
    print("Número inválido. Digite um número menor que 1000.")
else:
    centenas = num // 100
    dezenas = (num % 100) // 10
    unidades = (num % 100) % 10
    
    print(f"{centenas} {'centena' if centenas == 1 else 'centenas' if centenas > 1 else ''}, "
          f"{dezenas} {'dezena' if dezenas == 1 else 'dezenas' if dezenas > 1 else ''}, "
          f"{unidades} {'unidade' if unidades == 1 else 'unidades' if unidades > 1 else ''}")
