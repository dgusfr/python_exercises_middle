def comparar_strings(string1, string2):
    tamanho_string1 = len(string1)
    tamanho_string2 = len(string2)
    
    mesmo_comprimento = tamanho_string1 == tamanho_string2
    
    mesmo_conteudo = string1 == string2
    
    print(f'String 1: {string1}\nTamanho de "{string1}": {tamanho_string1} caracteres')
    print(f'String 2: {string2}\nTamanho de "{string2}": {tamanho_string2} caracteres')
    
    if mesmo_comprimento:
        print('As duas strings têm o mesmo comprimento.')
    else:
        print('As duas strings são de tamanhos diferentes.')
    
    if mesmo_conteudo:
        print('As duas strings possuem o mesmo conteúdo.')
    else:
        print('As duas strings possuem conteúdo diferente.')

string1 = "Brasil Hexa 2006"
string2 = "Brasil! Hexa 2006!"

comparar_strings(string1, string2)
