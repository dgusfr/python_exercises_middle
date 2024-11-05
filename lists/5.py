vetor = []

for i in range(20):
    numero = float(input(f"Digite o {i + 1}º número real: "))
    vetor.append(numero)

pares = [num for num in vetor if num % 2 == 0]
impares = [num for num in vetor if num % 2 != 0]

print("\nNúmeros digitados:")
print(vetor)

print("\nNúmeros pares:")
print(pares)

print("\nNúmeros ímpares:")
print(impares)