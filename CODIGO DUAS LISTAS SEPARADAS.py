# TODO: Crie uma função 'elementos_comuns' que receba duas listas de números inteiros separados por espaço:

def elementos_comuns(lista1, lista2):
    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))
    return list(set1.intersection(set2))

def conversor_int(lista):
    for item in lista:
        try:
            int(item)   ##aqui ele converte o item
        except ValueError:
            return False
    return True

# Leitura das listas
lista1 = input().split()
lista2 = input().split()

# Verifica se todas os elementos das listas podem ser convertidos para inteiros
if conversor_int(lista1) and conversor_int(lista2):

    comuns = elementos_comuns(lista1, lista2)
    
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")



#nao sei como funcionou
