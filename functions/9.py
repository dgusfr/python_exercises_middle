import re

def eh_palindromo(frase):
    frase_limpa = re.sub(r'[^a-zA-Z0-9]', '', frase.lower())
    return frase_limpa == frase_limpa[::-1]

frase_input = input("Informe uma frase para verificar se é um palíndromo: ")

if eh_palindromo(frase_input):
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
