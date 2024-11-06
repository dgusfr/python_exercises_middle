def somando(n1, n2, n3):
    return numero1 + numero2 + numero3

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))
numero3 = int(input("Informe o terceiro número: "))

print("A soma dos números é:", somando(numero1, numero2, numero3))

print("Usando listas e Laços:")
def calculaSoma(lista):
    return sum(lista)

numeros = []

for i in range(1, 4):
    numero = int(input(f"Informe o {i}° número: "))
    numeros.append(numero)

resultado = calculaSoma(numeros)
print("A soma dos números é:", resultado)


