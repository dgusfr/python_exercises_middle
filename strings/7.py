def validar_cpf(cpf):
    cpf_numerico = ''.join(filter(str.isdigit, cpf))

    if len(cpf_numerico) != 11:
        return False

    soma = 0
    for i in range(9):
        soma += int(cpf_numerico[i]) * (10 - i)
    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0

    soma = 0
    for i in range(10):
        soma += int(cpf_numerico[i]) * (11 - i)
    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0

    if int(cpf_numerico[9]) == digito1 and int(cpf_numerico[10]) == digito2:
        return True
    else:
        return False

cpf = input("Digite o CPF no formato xxx.xxx.xxx-xx: ")

if validar_cpf(cpf):
    print("O CPF é válido.")
else:
    print("O CPF NÃO é válido.")

