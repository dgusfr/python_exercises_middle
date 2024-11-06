import random

def embaralha_palavra(palavra):
    palavra = palavra.lower()

    # Embaralhar os caracteres
    caracteres_embaralhados = random.sample(palavra, len(palavra))

    # Juntar os caracteres embaralhados em uma string
    palavra_embaralhada = ''.join(caracteres_embaralhados)

    return palavra_embaralhada

# Solicitar entrada do usuário
palavra_input = input("Informe uma palavra: ")

# Chamar a função e imprimir o resultado
resultado = embaralha_palavra(palavra_input)
print(f"A palavra embaralhada é: {resultado}")
