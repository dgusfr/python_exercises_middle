meuVetor = [1, 2, 3, 4, 5]
print(meuVetor)

vetor = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    vetor.append(numero)

print("Números no vetor:")
for num in vetor:
    print(num)
