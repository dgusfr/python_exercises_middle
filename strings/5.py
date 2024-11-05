def imprimir_escada_invertida(nome):
    for i in range(len(nome), 0, -1):
        print(nome[:i].upper())

nome = input("Digite seu nome: ")
imprimir_escada_invertida(nome)