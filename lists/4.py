vetor = []

for i in range(10):
    caractere = input(f"Digite o {i + 1}º caractere: ")
    vetor.append(caractere)

consoantes = [c for c in vetor if c.isalpha() and c.lower() not in 'aeiou']

print("\nConsoantes lidas:")
for consoante in consoantes:
    print(consoante)

print(f"\nQuantidade de consoantes: {len(consoantes)}")

