import re

def eh_palindromo(frase):
    frase_limpa = re.sub(r'[^a-zA-Z0-9]', '', frase.lower())
    return frase_limpa == frase_limpa[::-1]
    # A função retorna True se a string limpa for igual à sua inversa, indicando que é um palíndromo

# Solicitar entrada do usuário
frase_input = input("Informe uma frase para verificar se é um palíndromo: ")

# Chamar a função e imprimir o resultado
if eh_palindromo(frase_input):
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
