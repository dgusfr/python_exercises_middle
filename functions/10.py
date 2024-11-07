def encontrar_fatorial(numero):
    fatorial = 1
    i = 1

    while fatorial < numero:
        i += 1
        fatorial *= i

    if fatorial == numero:
        print(f"{numero} = {i}!")
    else:
        print(f"{i - 1}! < {numero} < {i}!")

numero_input = int(input("Digite um número inteiro positivo: "))

encontrar_fatorial(numero_input)
