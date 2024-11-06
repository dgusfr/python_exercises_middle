def data_por_ext(data):
    try:
        dia, mes, ano = map(int, data.split('/'))

        if not (1 <= dia <= 31 and 1 <= mes <= 12):
            raise ValueError("Data inválida")

        meses = [
            "Janeiro", "Fevereiro", "Março", "Abril",
            "Maio", "Junho", "Julho", "Agosto",
            "Setembro", "Outubro", "Novembro", "Dezembro"
        ]

        formato_final = f"{dia} de {meses[mes - 1]} de {ano}"

        return formato_final
    except (ValueError, IndexError):
        return None

data_input = input("Informe a data no formato DD/MM/AAAA: ")

resultado = data_por_ext(data_input)
if resultado is not None:
    print(f"A data por extenso é: {resultado}")
else:
    print("Data inválida. Retornando NULL.")


#*****************************************
from datetime import datetime

def data_por_extenso(data):
    try:
        data_formatada = datetime.strptime(data, '%d/%m/%Y')

        formato_final = data_formatada.strftime('%d de %B de %Y')

        return formato_final
    except ValueError:
        return None

data_input = input("Informe a data no formato DD/MM/AAAA: ")

# Chamar a função e imprimir o resultado
resultado = data_por_extenso(data_input)
if resultado is not None:
    print(f"A data por extenso é: {resultado}")
else:
    print("Data inválida. Retornando NULL.")

