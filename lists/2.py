vetor = []

for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número real: "))
    vetor.append(numero)

print("Números na ordem inversa:")
for num in reversed(vetor):
    print(num)

print("Números na ordem inversa:")
for i in range(9, -1, -1):
    print(vetor[i])