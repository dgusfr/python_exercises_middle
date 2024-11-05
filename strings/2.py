def nomeContrarioMaiusculo (nome):
  nomeMaiusculo = nome.upper()
  nomeMaiusculoInvertido = nomeMaiusculo[::-1]
  print(nomeMaiusculoInvertido)

nome = input("Digite aqui o nome que deseja inverter:\n")
nomeContrarioMaiusculo(nome)
