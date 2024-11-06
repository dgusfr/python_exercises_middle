def imprimir_padrao(n):
    for i in range(1, n + 1):
        linha = ' '.join([str(i)] * i)
        print(linha)

valor_n = int(input("Informe um valor para n: "))
imprimir_padrao(valor_n)
