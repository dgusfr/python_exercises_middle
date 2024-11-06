import random

def embaralha_palavra(palavra):
    palavra = palavra.lower()

    caracteres_embaralhados = random.sample(palavra, len(palavra))

    palavra_embaralhada = ''.join(caracteres_embaralhados)

    return palavra_embaralhada

palavra_input = input("Informe uma palavra: ")

resultado = embaralha_palavra(palavra_input)
print(f"A palavra embaralhada é: {resultado}")
