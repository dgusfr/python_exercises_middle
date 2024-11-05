def validar_e_corrigir_telefone(telefone):
    telefone_numerico = ''.join(filter(str.isdigit, telefone))

    if len(telefone_numerico) == 7:
        telefone_corrigido = '3' + telefone_numerico
        return telefone_corrigido
    elif len(telefone_numerico) == 10:
        telefone_corrigido = '3' + telefone_numerico[1:]
        return telefone_corrigido
    else:
        return None

telefone = input("Telefone: ")

telefone_corrigido = validar_e_corrigir_telefone(telefone)

if telefone_corrigido:
    if len(telefone_corrigido) == 8:
        print("Telefone possui 7 dígitos. Acrescentarei o dígito três na frente.")
    else:
        print("Telefone já possui 8 dígitos.")

    print("Telefone corrigido sem formatação:", telefone_corrigido)

    telefone_formatado = telefone_corrigido[:4] + '-' + telefone_corrigido[4:]
    print("Telefone corrigido com formatação:", telefone_formatado)
else:
    print("Número de telefone inválido.")
