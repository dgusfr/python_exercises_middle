temperaturas = []

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]

for i in range(12):
    temperatura = float(input(f"Digite a temperatura média de {meses[i]}: "))
    temperaturas.append(temperatura)

media_anual = sum(temperaturas) / len(temperaturas)

print("\nMeses com temperaturas acima da média anual:")
for i in range(12):
    if temperaturas[i] > media_anual:
        print(f"{meses[i]} - Temperatura: {temperaturas[i]}")

print(f"\nMédia anual das temperaturas: {media_anual}")
