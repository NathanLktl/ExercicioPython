import random

palavras = ['amor', 'celular', 'computador', 'elefante', 'guitarra', 'internet', 'python', 'saudade' 'abacaxi', 'bicicleta', 'cachorro', 'diamante' , 'futebol' , 'girassol', 'hambúrguer' , 'igreja' , 'jardim', 'ketchup' , 'laranja' , 'maçã', 'navio', 'ovo', 'bola']

palavra = random.choice(palavras)

palavra_embaralhada = ''.join(random.sample(palavra, len(palavra)))

tentativas = 6

while tentativas > 0:
    print(f'A palavra embaralhada é: {palavra_embaralhada}')
    resposta = input('Qual é a palavra? ')
    if resposta == palavra:
        print('Parabéns! Você acertou a palavra!')
        break
    else:
        tentativas -= 1
        print(f'Resposta incorreta! Você ainda tem {tentativas} tentativas.')
else:
    print(f'Você perdeu! A palavra era "{palavra}".')
