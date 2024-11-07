def desenha_moldura(linhas=1, colunas=1):
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))

    for i in range(linhas):
        for j in range(colunas):
            if i == 0 or i == linhas - 1:
                # Primeira e última linha
                if j == 0 or j == colunas - 1:
                    print('+', end=' ')
                else:
                    print('-', end=' ')
            else:
                # Linhas internas
                if j == 0 or j == colunas - 1:
                    print('|', end=' ')
                else:
                    print(' ', end=' ')
        print()  # Nova linha entre as linhas

# Solicitar entrada do usuário
linhas_input = int(input("Informe o número de linhas (entre 1 e 20): "))
colunas_input = int(input("Informe o número de colunas (entre 1 e 20): "))

# Chamar a função e desenhar a moldura
desenha_moldura(linhas_input, colunas_input)
