# Para uma lista de n números, a pesquisa binária precisa de log de n na base 2 tentativas para retornar o valor correto

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1,3,5,7,9]
print(pesquisa_binaria(minha_lista,3)) # => 1
print (pesquisa_binaria(minha_lista,-1)) # => None