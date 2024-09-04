#INFORMANDO QUAIS SÃO AS VOGAIS
tabela_vogais = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

#FUNÇÃO CONTAR VOGAIS
def contar_vogais(texto):
    contagem = 0   
    for char in texto:
        if char in tabela_vogais:
            contagem += 1
    return contagem        
#entrada
texto = input()
#saida
resultado = contar_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")