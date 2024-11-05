import random
from re import A

def escolher_palavra():
    palavras = ['ABACAXI', 'BANANA', 'CACHORRO', 'GATO', 'ELEFANTE', 'GIRASSOL', 'PAPAGAIO', 'MORANGO']
    return random.choice(palavras)

def exibir_palavra_secreta(palavra, letras_certas):
    palavra_secreta = ''
    for letra in palavra:
        if letra in letras_certas:
            palavra_secreta += letra + ' '
        else:
            palavra_secreta += '_ '
    return palavra_secreta.strip()

def jogar_forca():
    palavra = escolher_palavra()
    letras_certas = set()
    tentativas = 0

    print("Bem-vindo ao jogo da Forca!")
    print("Tente adivinhar a palavra secreta.")

    while True:
        print("\nPalavra:", exibir_palavra_secreta(palavra, letras_certas))

        letra = input("Digite uma letra: ").upper()

        if letra in palavra:
            letras_certas.add(letra)
            print("Letra correta!")

            if set(palavra) == letras_certas:
                print("\nParabéns! Você venceu! A palavra era:", palavra)
                break
        else:
            tentativas += 1
            print(f"\n-> Você errou pela {tentativas}ª vez. Tente de novo!")

            if tentativas == 6:
                print("\nVocê foi enforcado! A palavra era:", palavra)
                break

jogar_forca()
