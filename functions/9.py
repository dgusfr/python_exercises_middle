import re

def eh_palindromo(frase):
    frase_limpa = re.sub(r'[^a-zA-Z0-9]', '', frase.lower())
    # r'[^a-zA-Z0-9]': Padrão que corresponde a qualquer caractere que não seja uma letra (maiúscula ou minúscula) ou número
    # frase.lower(): Converte a string para minúsculas antes de aplicar a substituição

    # Verificar se a string limpa é um palíndromo
    return frase_limpa == frase_limpa[::-1]
    # frase_limpa[::-1]: Inverte a string limpa
    # A função retorna True se a string limpa for igual à sua inversa, indicando que é um palíndromo

# Solicitar entrada do usuário
frase_input = input("Informe uma frase para verificar se é um palíndromo: ")

# Chamar a função e imprimir o resultado
if eh_palindromo(frase_input):
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
