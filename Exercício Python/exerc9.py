import random

def escolher_palavra():
    with open("palavras.txt", "r") as arquivo:
        palavras = arquivo.readlines()
    return random.choice(palavras).strip()

def verificar_letra(letra, palavra, letras_erradas, letras_certas):
    if letra in palavra:
        letras_certas.append(letra)
    else:
        letras_erradas.append(letra)

def imprimir_jogo(palavra, letras_certas):
    for letra in palavra:
        if letra in letras_certas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

def jogar_forca():
    palavra = escolher_palavra()
    letras_erradas = []
    letras_certas = []
    tentativas = 6
    
    while True:
        imprimir_jogo(palavra, letras_certas)
        print(f"Tentativas restantes: {tentativas}")
        letra = input("Digite uma letra: ").lower()
        
        verificar_letra(letra, palavra, letras_erradas, letras_certas)
        
        if letra not in palavra:
            tentativas -= 1
            
        if tentativas == 0:
            print("Você perdeu!")
            print(f"A palavra era {palavra}")
            break
        
        if set(palavra) == set(letras_certas):
            print("Parabéns! Você ganhou!")
            break

jogar_forca()
